# Puzzle Macro
puzzle macro

## Environment
* python 3.9
* selenium 4.1
* opencv-python
* pillow
* chrome 96

## Quick start
```shell
git clone https://github.com/ppd0523/puzzler
cd puzzler
python -m venv venv
pip install -r requirements.txt

python main.py
```

## Build Executable
This step confirmed Windows(10, 11), Mac OSX(15.0)
```shell
pip install pyinstaller
pyinstaller main.py --onefile --noconsole
```

## Running with Chrome extension
Creating the `extensions/`, place the `*.crx` as shown below
```shell
puzzler
├── README.md
├── extensions
│   └── metamask_10_6_4_0.crx
├── main.py
├── requirements.txt
├── tester.ipynb
└── tk2.py
```
