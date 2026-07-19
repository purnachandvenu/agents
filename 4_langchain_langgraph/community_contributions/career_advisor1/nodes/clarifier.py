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
        "def clarifier_node(state):\r\n",
        "    state[\"user_input\"][\"goal\"] = \"AI Engineer\"\r\n",
        "    state[\"clarified\"] = True\r\n",
        "    return state"
      ],
      "outputs": [],
      "execution_count": null
    }
  ]
}