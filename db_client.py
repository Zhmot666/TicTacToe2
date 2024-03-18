from abc import ABC, abstractmethod
import sqlite3
import psycopg2


class DB(ABC):
    # TODO: Дописать методы для логирования партий
    @abstractmethod
    def add_user(self):
        pass

    @abstractmethod
    def find_user(self):
        pass

    @abstractmethod
    def verify_user(self):
        pass


class SqliteDB(DB):
    __CONNECTION = sqlite3.connect('TicTacToe.db')

    def add_user(self):
        pass

    def find_user(self):
        pass

    def verify_user(self):
        pass


# class PostgresDB(DB):
#     __CONNECTION = psycopg2.connect('TicTacToe.db')
#
#     def add_user(self):
#         pass
#
#     def find_user(self):
#         pass
#
#     def verify_user(self):
#         pass


if __name__ == '__main__':
    pass
