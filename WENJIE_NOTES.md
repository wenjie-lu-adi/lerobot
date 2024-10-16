# Wenjie's Notes

## Setting up LeRobot Troubleshoots

### OpenGL Error

If you are like me, using this on a Mac, after you install the package and try to run:

```
import gymnasium
```

chances are you will get a "OpenGL no such file, not in dyld cache" error. This is because this package uses an older version of Mujoco which cannot find the right path for OpenGL. To fix it:

- locate the `cgl.py` file, usually at `/Users/{username}/Library/Caches/pypoetry/virtualenvs/lerobot-kQrwiUrd-py3.10/lib/python3.10/site-packages/mujoco/cgl/cgl.py`
- edit `cgl.py` with the right OpenGL path: `_CGL = ctypes.CDLL('/System/Library/Frameworks/OpenGL.framework/OpenGL')`
