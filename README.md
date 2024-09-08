# farm

## 一、开发参考
> 本项目是一个基于Flask的Web应用，前端使用Tailwind CSS。下述依赖版本请参考项目根目录下的`requirements.txt`文件以及`package.json`文件。

**前端**

Node.js + npm，然后，安装Tailwind CSS：

```bash
npm install -D tailwindcss
```

在项目根目录启动Tailwind编译进程：

```bash
npx tailwindcss -i ./src/app/static/css/input.css -o ./src/app/static/css/output.css --watch
```

**后端**

Python 3.9+，然后，安装Flask：

```bash
pip install Flask
```

以debug模式启动Flask：

```bash
flask --app ./src/run.py --debug run
```
