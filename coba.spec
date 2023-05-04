# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(['coba.py'],
             pathex=[],
             binaries=[],
             datas=[],
             hiddenimports=['tensorflow_core._api.v1.compat.v1.keras.callbacks', 'tensorflow_core._api.v1.compat.v2.keras.applications.mobilenet_v2', 'tensorflow_core._api.v1.compat.v1.keras.premade', 'tensorflow_core._api.v1.compat.v1.keras.applications.nasnet', 'tensorflow_core._api.v1.compat.v1.estimator.inputs', 'tensorflow_core._api.v1.compat.v1.keras.layers', 'tensorflow_core._api.v1.compat.v2.keras.initializers', 'tensorflow_core._api.v1.compat.v2.keras.constraints', 'tensorflow_core._api.v1.compat.v1.keras.datasets', 'tensorflow_core._api.v1.compat.v1.keras.utils', 'tensorflow_core._api.v1.compat.v1.keras.experimental', 'tensorflow_core._api.v1.compat.v1.keras.preprocessing.image', 'tensorflow_core._api.v1.compat.v2.keras.callbacks', 'tensorflow_core._api.v1.compat.v1.keras.datasets.cifar100', 'tensorflow_core._api.v1.compat.v2.keras.datasets', 'tensorflow_core._api.v1.compat.v1.keras.applications.imagenet_utils', 'tensorflow_core._api.v1.compat.v1.keras.datasets.imdb', 'tensorflow_core._api.v1.compat.v1.keras.backend', 'tensorflow_core._api.v1.compat.v1.estimator.tpu.experimental', 'tensorflow_core._api.v1.compat.v2.keras.applications.inception_resnet_v2', 'tensorflow_core._api.v1.compat.v2.keras.activations', 'tensorflow_core._api.v1.compat.v2.keras.applications.xception', 'tensorflow_core._api.v1.compat.v1.v1', 'tensorflow_core._api.v1.compat.v1.keras.applications.resnet50', 'tensorflow_core._api.v1.compat.v2.keras.premade', 'tensorflow_core._api.v1.compat.v1.keras.optimizers.schedules', 'tensorflow_core._api.v1.compat.v2.estimator.export', 'tensorflow_core._api.v1.compat.v2.keras.applications.imagenet_utils', 'tensorflow_core._api.v1.compat.v2.keras.preprocessing', 'tensor'],
             hookspath=[],
             hooksconfig={},
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)

exe = EXE(pyz,
          a.scripts, 
          [],
          exclude_binaries=True,
          name='coba',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=True,
          disable_windowed_traceback=False,
          target_arch=None,
          codesign_identity=None,
          entitlements_file=None )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas, 
               strip=False,
               upx=True,
               upx_exclude=[],
               name='coba')
