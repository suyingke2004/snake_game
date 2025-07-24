# Snake Gemini 🐍

这是一个使用 Python 和 Pygame 开发的经典贪吃蛇游戏。

## quick start

在release处下载.exe文件，点击即玩。

## ✨ 功能特性

*   **经典玩法**: 控制蛇吃食物，每吃一个食物，身体就会变长。
*   **动态计分**: 实时显示当前得分，每吃一个食物加10分。
*   **碰撞检测**: 游戏会在蛇撞到墙壁或自身时结束。
*   **游戏结束与重启**: 清晰的 "Game Over" 界面，显示最终得分。
*   **历史高分榜**: 自动保存并展示排名前5的历史高分记录。
*   **自定义UI**: 使用复古像素风格字体，提供 "Play Again" 和 "Quit" 按钮，支持鼠标点击。
*   **跨平台可执行**: 已使用 PyInstaller 打包，可在目标操作系统上直接运行。

## 🕹️ 玩法说明

*   **移动**: 使用 **方向键 (↑, ↓, ←, →)** 控制蛇的移动方向。
*   **目标**: 吃掉红色的食物，避免撞到墙壁或自己的身体。
*   **重新开始**: 在游戏结束后，点击 "Play Again" 按钮或按任意键可重新开始。
*   **退出**: 点击 "Quit" 按钮可退出游戏。

## 🛠️ 从源码构建和运行

如果您想从源码运行或修改本项目，请遵循以下步骤：

1.  **克隆仓库**
    ```bash
    git clone https://github.com/<Your-GitHub-Username>/snake_gemini.git
    cd snake_gemini
    ```

2.  **创建并激活 Conda 环境**
    ```bash
    # 创建环境
    conda create --name snake_game python=3.9 -y
    
    # 激活环境
    conda activate snake_game
    ```

3.  **安装依赖**
    ```bash
    # 安装 pygame
    conda install pygame -y
    ```
    或者，如果您不使用 Conda，可以使用 pip:
    ```bash
    pip install -r requirements.txt
    ```

4.  **运行游戏**
    ```bash
    python snake_game/main.py
    ```

## 📦 生成可执行文件 (.exe)

本项目使用 PyInstaller 进行打包。

1.  **安装 PyInstaller**
    ```bash
    conda install pyinstaller -y
    ```

2.  **运行打包命令 (在项目根目录)**
    > **重要**: 请在您想生成可执行文件的目标操作系统上运行此命令 (例如，在 Windows 上生成 `.exe`)。

    ```bash
    pyinstaller \
        --name snake_game \
        --onefile \
        --windowed \
        --add-data "snake_game/assets:assets" \
        snake_game/main.py
    ```

3.  **找到文件**
    生成的可执行文件将位于 `dist/` 目录下。

