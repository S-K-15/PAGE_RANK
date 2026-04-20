# 📊 PageRank Visualizer

A simple and interactive implementation of the **PageRank Algorithm** using Python.
This project demonstrates how web pages are ranked based on link structure, similar to how search engines like Google determine importance.

---

## 🚀 Features

* 📈 PageRank algorithm implementation
* 🌐 Graph-based representation of web pages
* 🎨 Visualization of node rankings
* ⚡ Interactive UI using Streamlit
* 🔄 Iterative rank updates

---

## 🧠 What is PageRank?

PageRank is an algorithm used to measure the importance of web pages based on the number and quality of links pointing to them.

> Pages with more important incoming links get higher ranks.

---

## 📁 Project Structure

```
pagerank-visualizer/
│── app.py            # Main Streamlit app
│── graph.py          # Graph creation logic
│── pagerank.py       # PageRank algorithm
│── visualize.py      # Graph visualization
│── requirements.txt  # Dependencies
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository

```
git clone https://github.com/S-K-15/PAGE_RANK.git
cd PAGE_RANK
```

### 2️⃣ Create virtual environment

```
python -m venv .venv
```

### 3️⃣ Activate environment

* Windows:

```
.venv\Scripts\activate
```

* Mac/Linux:

```
source .venv/bin/activate
```

### 4️⃣ Install dependencies

```
pip install -r requirements.txt
```

---

## ▶️ Run the Project

```
streamlit run app.py
```

---

## 📊 How It Works

1. Create a graph of web pages (nodes)
2. Define links between pages (edges)
3. Apply PageRank algorithm iteratively
4. Display ranks visually

---

## 🛠️ Technologies Used

* Python 🐍
* Streamlit 📊
* NetworkX 🌐
* Matplotlib 📉

---

## 🎯 Future Improvements

* Add real-world dataset support
* Improve UI/UX
* Export graph as image
* Add damping factor control

---

## 🤝 Contributing

Feel free to fork this repo and submit pull requests!

---

## 📜 License

This project is open-source and available under the MIT License.

---

## 👨‍💻 Author

**Kumar Saurav**

---

## ⭐ Support

If you like this project, consider giving it a star ⭐ on GitHub!
