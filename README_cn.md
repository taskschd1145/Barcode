# Barcode

## 许可证

本项目基于 MIT 许可证发布。详情请参阅 [LICENSE](LICENSE) 文件。

## 概述

本项目是一个使用Python编写的工具，旨在帮助用户快速批量生成条形码图片。它利用了 `python-barcode` 库来生成条形码，并使用 `Pillow` 库处理图片输出。

## 安装与配置

确保你已安装Python。如果未安装，请访问 [python.org](https://www.python.org/downloads/) 下载并安装最新版本。

在命令行中执行以下命令安装必要的Python包：

```bash
pip install Pillow
pip install python-barcode 
```

## 使用方法

### 1：获取源代码

从GitHub仓库的Releases部分或直接Git Clone下载源代码。

### 2：编辑条形码列表

打开 main.txt 文件，将其中的内容替换为你需要生成的条形码数据，每条数据占一行。

### 3：运行主脚本

在项目目录中，通过命令行运行 main.py 脚本：

```bash
python main.py
```

这将会根据 main.txt 中的数据生成条形码图片。
提示"Done."后就生成完成了

### 4：查看生成的图片

生成的条形码图片将被保存在 images 文件夹中。你可以在这里找到并使用这些图片。

### 5：清理

为了防止重复，建议在下次运行程序前删除 images 文件夹中的所有图片。

## 注意事项

默认情况下，条形码图片的尺寸为 600x400 像素。你可以在 main.py 文件中调整此设置。
### 注意：如有侵权行为，请通过[电子邮件](mailto:taskschd@hotmail.com)与我联系或者提 issue，我们会及时处理


