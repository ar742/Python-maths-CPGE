"""Échantillonnage, normalisations FFT, filtres et corrélations."""
import json
import math
import unittest
import numpy as np
from modeles_signal import amplitude_spectrum, alias_frequency, butterworth_response, causal_filter, MODELS
from catalogue_signal import LABS
from commun import clean

class SignalTests(unittest.TestCase):
    def test_sinusoid_exact_bin_amplitude(self):
        N=256;t=np.arange(N)/128
        for window in ('rect','hann','blackman'):
            f,a=amplitude_spectrum(1.7*np.cos(2*np.pi*13*t+.47),128,window)
            self.assertAlmostEqual(a[np.argmin(abs(f-13))],1.7,12)
    def test_dc_nyquist_not_doubled(self):
        for y in (np.ones(256)*3,(-1.)**np.arange(256)*3):
            _,a=amplitude_spectrum(y,128)
            self.assertAlmostEqual(a.max(),3,12)
    def test_parseval_dft_independent(self):
        rng=np.random.default_rng(3);y=rng.normal(size=129)
        z=np.fft.fft(y)
        self.assertAlmostEqual(float(np.sum(y*y)),float(np.sum(abs(z)**2)/len(y)),11)
    def test_alias_at_measurements_including_nyquist(self):
        for F in (8,24,80):
            for f in (0,1,12,19,24,80):
                k=np.arange(50);a=alias_frequency(f,F)
                np.testing.assert_allclose(np.sin(2*np.pi*f*k/F+.9),np.sin(2*np.pi*a*k/F+.9),atol=2e-13)
    def test_butterworth_magnitude_poles_and_dc(self):
        for n in range(1,7):
            f=np.array([0,5,10,70]);h=butterworth_response(f,10,n)
            np.testing.assert_allclose(abs(h),1/np.sqrt(1+(f/10)**(2*n)),rtol=3e-14,atol=2e-15)
            self.assertAlmostEqual(h[0].real,1,13)
    def test_causal_fir_noise_variance(self):
        impulse=np.r_[1.,np.zeros(100)]
        h=causal_filter(impulse,'mean',9)
        self.assertAlmostEqual(np.sum(h),1)
        self.assertAlmostEqual(np.sum(h*h),1/9)
    def test_recursive_dc_and_noise_variance(self):
        a=math.exp(-1/9);h=causal_filter(np.r_[1.,np.zeros(1000)],'rc',9)
        self.assertAlmostEqual(np.sum(h),1,13)
        self.assertAlmostEqual(np.sum(h*h),(1-a)/(1+a),13)
    def test_correlation_peak_sign_and_distance(self):
        lab=next(l for l in LABS if l['id']=='correlation_retard');p={c['key']:c['value'] for c in lab['controls']};p.update(delay=.6,noise=0,speed=350)
        r=MODELS[lab['id']](p);metrics={m['label']:m['value'] for m in r['metrics']}
        self.assertAlmostEqual(metrics['Retard estimé'],.6)
        self.assertAlmostEqual(metrics['Distance aller-retour estimée'],105)
        self.assertAlmostEqual(metrics['Maximum de corrélation normalisée'],1,9)
    def test_poisson_dual_gaussian_accuracy(self):
        r=MODELS['poisson_gaussienne']({'sigma':.3,'T':1.5,'N':20})
        self.assertLess(r['metrics'][0]['value'],1e-12)
    def test_shannon_more_samples_improves_interior(self):
        first=MODELS['shannon']({'F':24,'B':3,'f0':5,'M':8})
        last=MODELS['shannon']({'F':24,'B':3,'f0':5,'M':100})
        self.assertLess(last['metrics'][3]['value'],first['metrics'][3]['value']/50)
    def test_spectrogram_analytic_ridge_and_finite_values(self):
        r=MODELS['spectrogramme']({'length':48,'f0':8,'f1':48});sc=r['scene']
        estimated=sc['frequencies'][np.argmax(sc['db'],axis=0)]
        np.testing.assert_allclose(estimated,sc['ridge'],atol=1)
        self.assertTrue(np.isfinite(sc['db']).all())
    def test_defaults_presets_and_extremes_are_exportable(self):
        for lab in LABS:
            default={c['key']:c['value'] for c in lab['controls']}
            cases=[default]+[{**default,**p['values']} for p in lab['presets']]
            for key in ('min','max'):
                cases.append({c['key']:c[key] if key in c else c['value'] for c in lab['controls']})
            for p in cases:
                with self.subTest(lab=lab['id'],p=p):
                    r=clean(MODELS[lab['id']](p));json.dumps(r,allow_nan=False)
                    self.assertTrue(r['steps']);self.assertTrue(r['assumptions'])

if __name__=='__main__':unittest.main()
