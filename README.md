# :book: Books

## :dog: Introduction:
- Welcome to this repository, where you'll find an extensive collection of books
conveniently hosted in one place. The goal is to make it easy for you to explore
and access a diverse range of literary works.

- Due to GitHub's invalidation of file uploads above 100MB, certain books in this 
repository have been compressed with the `.xz` extension. This repository includes 
Python scripts specifically designed to manage and handle this limitation in `/bin/` directory.


## :cat: For download books

- Firstly, clone the repo:

```sh
git clone https://github.com/hungpham3112/Books.git && cd Books
```

- Secondly, extract some compressed books (Python is required)

```python
python bin\extract.py
```

- Enjoy:tada::tada::tada:

## :fish: For uploads books

- Firstly, check if there are files more than 100MB

```python
python bin\find.py
```

- Secondly, compress book to `.xz` extension (Duration will depend on the file size.)

```python
python bin\compress.py
```

