# ANTLR4 PoC

This is a demo project for PoC on [ANTLR4](https://github.com/antlr/antlr4/blob/master/doc/index.md).

## Setup Requirements

Follow the instructions from official documentation to [setup](https://github.com/antlr/antlr4/blob/master/doc/python-target.md)

## How to run this project

You can pull and setup project in your local

##### Install requiremets 

```
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
```
##### Translate grammer file to your target language

```
    antlr4 -Dlanguage=Python3 writeprogram.g4
```
##### Update your commands in `commands.txt`
```
    TargetLanguage:
    Instruction1
    Instruction2
    .
    .
    Instructionn
```
##### Generate your Desired Code

```
    python3 main.py commands.txt
```