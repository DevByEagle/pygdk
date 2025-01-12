 # Pygdk
 
 <!-- ![PyPI](https://img.shields.io/pypi/v/pygdk)
 ![License](https://img.shields.io/github/license/DevByEagle/pygdk)   -->

**Pygdk** is a powerful, lightweight, and easy-to-use Python Gui library.

---

## 📦 Installation

Install **Pygdk** directly from PyPI:

```bash
pip install pygdk
```

Or install the latest development version:

```bash
pip install git+https://github.com/DevByEagle/pygdk.git
```

---

## 🛠️ Usage

Start using **Pygdk** with minimal setup:

```python
import pygdk

window = pygdk.Surface(pygdk.Vector2(800, 600), "Example")
pygdk.drawText(window, "Hello World", None, None)
window.show()
```
