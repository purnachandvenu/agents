{
  "nbformat": 4,
  "nbformat_minor": 5,
  "metadata": {
    "kernelspec": {
      "display_name": "Python 3",
      "language": "python",
      "name": "python3"
    },
    "language_info": {
      "name": "python",
      "version": "3.10.0"
    }
  },
  "cells": [
    {
      "cell_type": "code",
      "metadata": {},
      "source": [
        "import warnings\r\n",
        "import gradio as gr\r\n",
        "from demo.ui import create_ui\r\n",
        "from demo.util import css, js\r\n",
        "\r\n",
        "# Gradio 6.14 reads a Starlette status constant that newer Starlette has renamed, so it warns on\r\n",
        "# every request. Silence that upstream deprecation so the dashboard console stays clean.\r\n",
        "warnings.filterwarnings(\"ignore\", message=\".*HTTP_422_UNPROCESSABLE_ENTITY.*\")\r\n",
        "\r\n",
        "if __name__ == \"__main__\":\r\n",
        "    ui = create_ui()\r\n",
        "    ui.launch(\r\n",
        "        theme=gr.themes.Default(primary_hue=\"sky\"),\r\n",
        "        css=css,\r\n",
        "        js=js,\r\n",
        "        inbrowser=True,\r\n",
        "    )\r\n",
        ""
      ],
      "outputs": [],
      "execution_count": null
    }
  ]
}