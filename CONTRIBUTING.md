## Setting up the project

1. [Fork](https://help.github.com/articles/fork-a-repo/) the project, clone your fork, and configure the remotes:

```bash
# Clone your fork of the repo into the current directory
git clone https://github.com/<your-username>/atri_python_assignment.git
# Navigate to the newly cloned directory
cd atrilabs-engine
# Assign the original repo to a remote called "upstream"
git remote add upstream https://github.com/Atri-Apps/atri_python_assignment.git
```

2. Install python dependencies

```bash
# Run the following command from the root directory of your project
pipenv install
```

3. Start the virtual environment

```bash
pipenv shell
```

4. Start the atri development server

```bash
atri start
```

The Atri visual editor will start in `localhost:4002` automatically. If it doesn't then open your browser (Chrome preferrably) and visit `http://localhost:4002`.

5. Press `Build & Run` on the top right corner of the Atri visual editor.

On pressing `Build & Run` for the first time, it will take few minutes to complete the installation of some packages from PyPi and npm.

6. Once `Build & Run` completes, open the project directory in your favourite code editor to begin writing the backend code.
