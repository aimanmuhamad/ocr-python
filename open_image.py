{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "open_image.ipynb",
      "provenance": [],
      "authorship_tag": "ABX9TyPzR+pm03921nEo9R6Dg90z"
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "code",
      "execution_count": 3,
      "metadata": {
        "id": "4ILPCdK0xJCl"
      },
      "outputs": [],
      "source": [
        "from PIL import Image"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "im_file = \"page09.jpg\""
      ],
      "metadata": {
        "id": "fiJZytGoxVLw"
      },
      "execution_count": 4,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "im = Image.open(im_file)\n",
        "print(im.size)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "PKlDxTtlxX8j",
        "outputId": "13cfc6e5-d029-41a5-cc89-6b4c79b96041"
      },
      "execution_count": 6,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "(2460, 3280)\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "im.rotate(180).show()"
      ],
      "metadata": {
        "id": "pBrFeK3Ixfek"
      },
      "execution_count": 9,
      "outputs": []
    }
  ]
}