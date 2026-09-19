# Zadanie 1
# def max_value_key(dictionary):
#     return max(dictionary, key=dictionary.get)
#
#
# def main():
#     example_dict = {'a' : 10, 'b' : 20, 'c' : 5}
#     print(max_value_key(example_dict))
#
#
#
# if __name__ == '__main__':
#     main()
# Zadanie 2
# def count_vovels(text):
#     x = 0
#     samogloski = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
#     for c in text:
#         if c in samogloski:
#             x += 1
#     return x
#
# def main():
#     example_text = "Hello World!"
#     print(count_vovels(example_text))
#
# if __name__ == '__main__':
#     main()
# Zadanie 3
#
# def rotate_sublists(lst, n):
#     for i in range(0, len(lst), n):
#         if i + n <= len(lst):
#             lst[i:i + n] = lst[i:i + n][::-1]
#     return lst
#
#
# def main():
#     example_list = [1,2,3,4,5,6,7,8]
#     n = 2
#     print(rotate_sublists(example_list, n))
#
#
# if __name__ == '__main__':
#     main()
#
#
#
# Zadanie 4
#
# def main():
#     with open("tekst.txt", "r") as plik1:
#         text = plik1.read()
#
#     podstawienia = {}
#     with open("podstawienia.txt", "r", encoding="utf-8") as plik2:
#         for linia in plik2:
#             if not linia:
#                 continue
#
#             linia = linia.strip()
#
#             znak1, znak2 = linia.split("->")
#             podstawienia[znak1] = znak2
#
#     zaszyfrowane = ""
#     for c in text:
#         if c in podstawienia:
#             zaszyfrowane += podstawienia[c]
#         else:
#             zaszyfrowane += c

#     with open("zaszyfrowane.txt", "w", encoding="utf-8") as plik3:
#         plik3.write(zaszyfrowane)
#
#
# if __name__ == '__main__':
#     main()
#
# #Zadanie 5
#
# class Book:
#     def __init__(self, title, author):
#         self.title = title
#         self.author = author
#
#
# class Library:
#     def __init__(self):
#         self.books = []
#
#     def loadBook(self):
#         with open("books.txt", "r", encoding="utf-8") as file:
#             for line in file:
#                 if  line is None:
#                     continue
#                 title, author = line.strip().split(",")
#                 self.books.append(Book(title, author))
#
#     def addBook(self):
#         title = input("Enter book title: ")
#         author = input("Enter book author: ")
#         self.books.append(Book(title, author))
#
#     def deleteBook(self):
#        title = input("Enter book title: ")
#
#        for book in self.books:
#             if book.title == title:
#                 self.books.remove(book)
#                 return
#
#     def showBooks(self):
#         for book in self.books:
#             print(book.title, ",", book.author)
#
#
# def main():
#     library = Library()
#     library.loadBook()
#     library.showBooks()
#     library.addBook()
#     library.showBooks()
#     library.deleteBook()
#     library.showBooks()
#
# if __name__ == "__main__":
#     main()
#
# Zadanie 6
#
# class Student:
#     def __init__(self, imie, nazwisko, ocena):
#         self.imie = imie
#         self.nazwisko = nazwisko
#         self.ocena = int(ocena)
#
#     def __str__(self):
#         return f"{self.imie} {self.nazwisko} {self.ocena}"
#
# class Group:
#      def __init__(self):
#          self.students = []
#
#      def add_students(self):
#          with open("students.txt", "r", encoding="utf-8") as file:
#              for line in file:
#                  if line.strip == "":
#                      continue
#                  imie, nazwisko, ocena = line.strip().split(",")
#                  self.students.append(Student(imie, nazwisko, ocena))
#
#      def show_students(self):
#          for student in self.students:
#              print(student)
#
#      def findStudent(self):
#          nazwisko = input("Podaj nazwisko: ")
#          for student in self.students:
#              if student.nazwisko == nazwisko:
#                  print(student.imie, nazwisko, student.ocena)
#              else:
#                  print("Nie znaleziono studenta.")
#
#      def betterGrades(self, x):
#          for student in self.students:
#              if student.ocena > x:
#                  print("Oceny studenta/ow wieksze lub rowne od", x, ":")
#                  print(student)
#
#
# def main():
#     print("1. Pokaz studentow\n 2. Znajdz studenta\n 3. Pokaz jacy studenci maja lepszą ocene od podanej przez ciebie.")
#     group = Group()
#     group.add_students()
#     x = int(input("Jaką akcje chcesz wykonać?:" ))
#     match x:
#         case 1:
#             group.show_students()
#         case 2:
#             group.findStudent()
#         case 3:
#             y = int(input("Podaj ocene: "))
#             group.betterGrades(y)
#
# if __name__ == "__main__":
#     main()
#
# Zadanie 7
#
#
# def count_digits(text):
#     count = 0
#     digits = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
#     for c in text:
#         if c in digits:
#             count += 1
#     return count
#
# def main():
#     text = input("Wpisz tekst: ")
#     print(count_digits(text))
#
# if __name__ == '__main__':
#     main()
#
# Zadanie 8
#
# def sumSublists(list, n):
#     wynik = []
#     for i in range(0, len(list), n):
#         if i + n <= len(list):
#             wynik.append(sum(list[i:i+n]))
#     return wynik
#
# def main():
#     list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#     n = 3
#     print(sumSublists(list2, n))
#
# if __name__ == '__main__':
#     main()
#
# Zadanie 9
#
# def main():
#     with open("tekst.txt", "r", encoding="utf-8") as f:
#         text = f.read()
#
#
#     podstawienia = {}
#     with open("podstawienia.txt", "r", encoding="utf-8") as f2:
#         for line in f2:
#             if not line:
#                 continue
#             line = line.strip()
#
#             znak1, znak2 = line.split("->")
#             podstawienia[znak1] = znak2
#
#     wynik = ""
#
#     for c in text:
#         if c in podstawienia:
#             wynik += podstawienia[c]
#         else:
#             wynik += c
#
#     with open("zaszyfrowane2.txt", "w", encoding="utf-8") as f:
#         f.write(wynik)
#
#
#
#
#
# if __name__ == '__main__':
#     main()
#
# # Zadanie 10
# class Movie:
#     def __init__(self, movie, director, year):
#         self.movie = movie
#         self.director = director
#         self.year = int(year)
#
#     def __str__(self):
#         return f"{self.movie} {self.director} {self.year}"

# class MovieLibrary:
#     def __init__(self):
#         self.movieLibrary = []
#
#     def showMovies(self):
#         for movie in self.movieLibrary:
#             print(movie)
#
#
#     def findMovieByDirector(self):
#         findingDirector = input("Enter Director: ")
#         for movie in self.movieLibrary:
#             if movie.director == findingDirector:
#                 print(movie)
#     print("I didnt find this director and his movie")
#
#     def findNewerMovieByYear(self):
#         findingYear = int(input("Enter Year: "))
#         for movie in self.movieLibrary:
#             if movie.year >= findingYear:
#                 print(movie)
#     print("I didnt find a movie newer than this year")
#
#
#
# def main():
#     ml = MovieLibrary()
#
#     with open("movies.txt", "r", encoding="utf-8") as moviesfile:
#         for line in moviesfile:
#             if line is None:
#                 continue
#             line = line.strip()
#             movie, director, year = line.split(",")
#             ml.movieLibrary.append(Movie(movie, director, year))
#
#     print("What you want to do?")
#     print("1. Show all movies in your library\n")
#     print("2. Find a movie by a director\n")
#     print("3. Find a movie by a year\n")
#     print("4. Exit program\n")
#
#     while True:
#         x = int(input("Enter your choice: "))
#
#         match x:
#             case 1:
#                 ml.showMovies()
#             case 2:
#                 ml.findMovieByDirector()
#             case 3:
#                 ml.findNewerMovieByYear()
#             case 4:
#                 break
#
# if __name__ == "__main__":
#     main()


#Zadanie 11

def count_words(text):
    counted_words = {}
    text = text.lower()

    for word in text.split():
        if word not in counted_words:
            counted_words[word] = 1
        else:
            counted_words[word] += 1
    return counted_words

def main():
    text = input("Enter a text: ")
    print(count_words(text))

if __name__ == "__main__":
    main()


