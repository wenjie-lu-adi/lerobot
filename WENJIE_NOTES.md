# Wenjie's Notes

## Quick Start

To see live camera view (handy when adjusting camera angle):

```sh
python lerobot/scripts/webcam_live.py
```

To test tele-op:

```sh
python lerobot/scripts/control_robot.py teleoperate \
  --robot-path lerobot/configs/robot/koch-office.yaml \
```

To start or resume a data collection session:

```sh
python lerobot/scripts/control_robot.py record \
  --robot-path lerobot/configs/robot/koch-office.yaml \
  --fps 30 \
  --root data \
  --repo-id 2024-1104-push-t/run01 \
  --tags wenjie \
  --warmup-time-s 5 \
  --episode-time-s 30 \
  --reset-time-s 10 \
  --num-episodes 10 \
  --push-to-hub 0
```

To visualize collected dataset:

```sh
python lerobot/scripts/visualize_dataset_html.py \
  --root data \
  --repo-id 2024-1104-push-t/run01
```

## Setting up LeRobot Troubleshoots

### OpenGL Error

If you are like me, using this on a Mac, after you install the package and try to run:

```
import gymnasium
```

chances are you will get a "OpenGL no such file, not in dyld cache" error. This is because this package uses an older version of Mujoco which cannot find the right path for OpenGL. To fix it:

- locate the `cgl.py` file, usually at `/Users/{username}/Library/Caches/pypoetry/virtualenvs/lerobot-kQrwiUrd-py3.10/lib/python3.10/site-packages/mujoco/cgl/cgl.py`
- edit `cgl.py` with the right OpenGL path: `_CGL = ctypes.CDLL('/System/Library/Frameworks/OpenGL.framework/OpenGL')`
