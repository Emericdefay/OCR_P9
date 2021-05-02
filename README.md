<p align="center">
  <a href="127.0.0.1:8000">
    <img width=200px height=200px src="https://user.oc-static.com/upload/2020/09/18/16004297044411_P7.png" alt="LITReview logo">
  </a>
</p>

<h3 align="center">LITReview Website Project</h3>

---

<p align="center"> This projet is a first approach to django, proposed by OCR.
    <br> 
</p>

## 📝 Table of Contents

- [About](#about)
- [Getting Started](#getting_started)
- [Usage](#usage)
- [Built Using](#built_using)
- [Authors](#authors)

## 🧐 About <a name = "about"></a>
<p>
This projet is a first approach to django.<br>
It contains several idioms to discover:
<ul>
  <li>authentification</li>
  <li>Models manipulation, union, intersection</li>
  <li>Forms manipulation</li>
  <li>django template language with blocks, conditions, filters...</li>
  <li>bootstrap </li>
  <li>POO surcharge</li>
  <li>django ORM in general
  <li>security</li>
</ul>
All stuff needed to create a web project.
</p>

## 🏁 Getting Started <a name = "getting_started"></a>

<p>We need to setup our environment to launch our web project.</p>

### Prerequisites

<p>
First, you have to ensure that your python version is <strong>3.6</strong> or higher.<br>
For more informations, check the <a href="#built_using">Built Using section</a>.
</p>

### Setup our environment

#### Step 1.
Create a new folder and execute this command from it.
It clones the git project in your folder.

```
git clone https://github.com/Emericdefay/OCR_P9.git
```
#### Step 2.
Create a virtuel environment with venv.

```
python -m venv env
```
#### Step 3.
Start your environment.

On windows:

```
env\Scripts\activate.bat
```

On linux:

```
source env\Scripts\activate
```
#### Step 4.
Go to the root of the project.

```
cd OCR_P9/
```
#### Step 5.
Install requirements

```
pip install -r requirements.txt
```
#### Step 6.
Go inside the project

```
cd LITReview/
```
#### Step 7.
start env next time

```
python manage.py runserver
```

### Done!
<p>
Now the next time you want to run the local server <br>
Launch the terminal from your folder created at step 1<br>
<strong>Then repeat the step 3</strong> and launch:</p>

```
python OCR_P9/LITReview/manage.py runserver
```

## 🎈 Usage <a name="usage"></a>

django runserver

```
cmd
```

if port already taken, 8080

```
cmd
```

## ⛏️ Built Using <a name = "built_using"></a>

- [sqlite3](https://www.sqlite.org/index.html) - Database
- [Django](https://www.djangoproject.com/) - Web Framework
- [Bootstrap](https://getbootstrap.com/) - Toolkit

## ✍️ Authors <a name = "authors"></a>

- [@emericdefay](https://github.com/emericdefay) - Author of the solution.
