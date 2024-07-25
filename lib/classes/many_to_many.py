class Article:
    all = []

    def _init_(self, author, magazine, title):
        if not isinstance(author, Author):
            raise ValueError("Author must be an instance of Author")
        if not isinstance(magazine, Magazine):
            raise ValueError("Magazine must be an instance of Magazine")
        if not isinstance(title, str) or len(title) < 5 or len(title) > 50:
            raise ValueError("Article title must be a string between 5 and 50 characters")
        self._title = title
        self._author = author
        self._magazine = magazine
        self._author._articles.append(self)
        self._magazine._articles.append(self)
        Article.all.append(self)

    @property
    def title(self):
        return self._title

    @title.setter

    def title(self, value):

        raise AttributeError("Can't set attribute, title is immutable")    

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        if not isinstance(value, Author):
            raise ValueError("Author must be an instance of Author")
        self._author._articles.remove(self)
        self._author = value
        value._articles.append(self)

    @property
    def magazine(self):
        return self._magazine

    @magazine.setter
    def magazine(self, magazine):
        if not isinstance(magazine, Magazine):
            raise ValueError("Magazine must be an instance of Magazine")
        self._magazine._articles.remove(self)
        self._magazine = magazine
        magazine._articles.append(self)


class Author:
    def _init_(self, name):
        if not isinstance(name, str):
            raise TypeError("Name must be of type str")
        if len(name) == 0:
            raise ValueError("Name must be a non-empty string.")
        self.__name = name
        self._articles = []

    @property
    def name(self):
        return self.__name

    
    def _setattr_(self, key, value):
        if hasattr(self, key):
            raise AttributeError("Can't modify author's name after instantiation")
        super()._setattr_(key, value)

    def articles(self):
        return self._articles

    def magazines(self):
        return list({article.magazine for article in self._articles})

    def add_article(self, magazine, title):
        new_article = Article(self, magazine, title)
        return new_article

    def topic_areas(self):
        if not self._articles:
            return None
        return list({article.magazine.category for article in self._articles})


class Magazine:
    _magazines = []

    def _init_(self, name, category):
                
        self._name = name
        self._category = category
        self._articles = []
        Magazine._magazines.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and 2<= len(value) <= 16:
            self._name = value

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, category):
        if isinstance(category, str) and len(category) > 0:
            self._category = category   

    def articles(self):
        return self._articles

    def contributors(self):
        return list(set(article.author for article in self._articles))

    def article_titles(self):
        if not self._articles:
            return None
        return [article.title for article in self._articles]

    def contributing_authors(self):
        if not self._articles:
            return None
        author_counts = {}
        for article in self._articles:
            if article.author not in author_counts:
                author_counts[article.author] = 0
            author_counts[article.author] += 1
        contributing_authors = [author for author, count in author_counts.items() if count > 2]

        return contributing_authors if contributing_authors else None