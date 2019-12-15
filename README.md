[![CircleCI](https://circleci.com/gh/FabriSilve/LambdaBot/tree/master.svg?style=svg)](https://circleci.com/gh/FabriSilve/LambdaBot/tree/master)
[![codebeat badge](https://codebeat.co/badges/89e46975-18a7-4de3-824e-a7ecd69210e8)](https://codebeat.co/projects/github-com-fabrisilve-lambdabot-master)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/18b231f6602c44d098e12dc8b57d7d44)](https://www.codacy.com/manual/FabriSilve/LambdaBot?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=FabriSilve/LambdaBot&amp;utm_campaign=Badge_Grade)
[![Codacy Badge](https://api.codacy.com/project/badge/Coverage/18b231f6602c44d098e12dc8b57d7d44)](https://www.codacy.com/manual/FabriSilve/LambdaBot?utm_source=github.com&utm_medium=referral&utm_content=FabriSilve/LambdaBot&utm_campaign=Badge_Coverage)

# Lambda Telegram Bot
> AWS Lambda Telegram Bot

---

## Development

### Python environment
> Install python 3 locally

With Homebrew:

```sh
brew install python3
```

With Pacman

```sh
pacman -S python-pip
```

> Create virtual environment

```sh
python(3) -m venv <path/envirnoment>
```

> Activate virtual environment from inside environment directory

```sh
source bin/activate
```

> Clone git repository

```sh
git clone <repo-url>
```

> Install dependency from inside project directory

```sh
pip(3) install -r requirements.txt
```

---

### Pull requests rules
- All commits have to be signed
- All pull requests need a code owner review
- All pull request need to be rebased on the last `master` version before merge them
- All pull request have to pass tests and quality code check
- The `master` branch need to keep code coverage over **85%**
- The `master` branch need to keep code quality **A**

---

### Deploy
> The lambda is automatically deployed when a pull request is merged on the `master` branch
