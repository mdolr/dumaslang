# DUMASLang

DUMASLang is a language based on the gimmicks of [Chef Michel DUMAS](https://www.youtube.com/c/ChefMichelDumas) in his YouTube videos.

This is just a fun little side-project done while building a python meta-compiler for class.

## Install

```
git clone
```

## Run

The command takes 2 arguments :

- The path to your file
- Optional: A grammar name without the .txt if you want to use your own grammar (add it in the grammars folder) -> This is a metacompiler so it can compile any correct grammar

```sh
python main.py </path/to/file> <optional: grammar_name>

sh dumas.sh </path/to/file> <optional: grammar name>

dumas </path/to/file> <optional: grammar name> # you need to set an alias pointing to dumas.sh first
```

## Syntax

Check the different examples available in the `examples` folder

### Program structure

Just like every chef's video our program starts with :

```
Salut les amis bienvenue à la maison
```

and ends with :

```
Maitre d'hotel le plat de la table 55 est prêt on enlève!
```

### Defining variables

⚠️ In this language all variables are global variables.

To define variables use the syntax below - [Types and examples here](/examples/variables.dumas)

```
je réserve variable_name = value
```

User inputs can be entered using :

```
je réserve user_input = je lis tous les commentaires
```

The input has to be formatted as it would in the program (e.g strings have to be between double quotes)

### Conditions

Compare 2 symbols, symbols can be one of the followings :

- strings
- integers
- floats
- variables

(so no calculations or user inputs)

```
symbol1 == symbol2
symbol1 != symbol2
symbol1 <= symbol2
symbol1 >= symbol2
symbol1 < symbol2
symbol1 > symbol2
```

### Loops

Only while loops are implemented

```
je réserve i = 0

tourne et retourne tant que Condition
    je réserve i = on calcule i + 1
comme ça
```

### If / Else

Only ifs and elses have been implemented so in order to make an "else if" statement you have to combine multiple ifs and elses. See the [example](/examples/if_else.dumas)

The syntax is the following for a simple if statement

```
contrôle de la qualité Condition
    on dresse "condition is ok"
terminé
```

The syntax for an if/else

```
contrôle de la qualité Condition
    on dresse "condition is met"
sinon c'est pas encore bon
    on dresse "condition not met"
terminé
```

### Functions

[Example of a recursive function](/examples/functions.dumas)

Functions are declared with the following syntax

```
Machine miracle hello_world :
    on dresse "Hello world! :D"
en effet c'est prêt
```

You can also pre-declare variables to avoid errors

```
Machine miracle addition on mélange a et b :
    je réserve c = on calcule a + b
en effet c'est prêt
```

To call a function you don't need to give the parameters they should be declared before calling the function

```
Feu allume hello_world !

je réserve a = 3
je réserve b = 4

Feu allume addition !
on dresse c
```
