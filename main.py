import psycopg2
from pprint import pprint

print("Добро пожаловать в программу для управления клиентами! \nПожалуйста,введите необходимую команду из предложенного списка, \nа затем выполните необходимое Вам действие")
print("Для создания структуры БД (таблицы) введите  0")
print("Для добавления нового клиента введите  1")
print("Для добавления телефона для существующего клиента введите  2")
print("Для изменения имени клиента введите  3")
print("Для изменения фамилии клиента введите  4")
print("Для изменения e-mail клиента введите  5")
print("Для изменения номера телефона клиента введите  6")
print("Для удаления номера телефона существующего клиента введите  7")
print("Для удаления существующего клиента введите  8")
print("Для поиска существующего клиента по его данным введите  9")


conn = psycopg2.connect(host="127.0.0.1", user="postgres", password="***", database="HomeWork5", port="5432")


def create_tables():
    '''Создание таблиц клиентских данных'''
    with conn.cursor() as cur:
        #Создание таблицы основных клиентских данных
        cur.execute("""
        CREATE TABLE IF NOT EXISTS clients_Homework5(
        id SERIAL PRIMARY KEY, 
        client_name VARCHAR(100) NOT NULL, 
        client_surname VARCHAR(100) NOT NULL, 
        client_email VARCHAR(100) NOT NULL
        );
        """)
        #Создание отдельной таблицы с клиентскими номерами
        cur.execute("""
        CREATE TABLE IF NOT EXISTS client_phonenumbers(
        id_phonenumber SERIAL PRIMARY KEY,
        client_id INTEGER NOT NULL REFERENCES clients_Homework5(id),
        client_phonenumber INTEGER UNIQUE);
        """)
        conn.commit()

#create_tables()



def add_new_client():
    '''Добавление нового клиента в таблицу clients_Homework5'''
    input_client_name = input("Введите имя клиента для добавления в таблицу: ")
    input_client_surname = input("Введите фамилию клиента для добавления в таблицу: ")
    input_client_email = input("Введите email клиента для добавления в таблицу: ")
    with conn.cursor() as cur:
        cur.execute("""
        INSERT INTO clients_Homework5(client_name, client_surname, client_email) VALUES(%s, %s, %s);
        """, (input_client_name, input_client_surname, input_client_email))
        conn.commit()

#add_new_client()



def add_new_phonenumber():
    '''Добавление нового номера телефона в таблицу client_phonenumbers'''
    input_client_id = input("Введите id клиента для добавления номера телефона: ")
    input_phonenumber = input("Введите номер телефона для добавления: ")
    with conn.cursor() as cur:
        cur.execute("""
        INSERT INTO client_phonenumbers(client_id, client_phonenumber) VALUES(%s, %s);
        """, (input_client_id, input_phonenumber))
        conn.commit()

#add_new_phonenumber()



def change_client_name():
    '''Изменение имени клиента в таблице clients_Homework5'''
    input_id_for_changing_name = input("Введите id клиента имя которого хотите изменить: ")
    input_name_for_changing = input("Введите имя для изменения: ")
    with conn.cursor() as cur:
        cur.execute("""
        UPDATE clients_Homework5 SET client_name=%s WHERE id=%s;
        """, (input_name_for_changing, input_id_for_changing_name))
        conn.commit()

#change_client_name()



def change_client_surname():
    '''Изменение фамилии клиента в таблице clients_Homework5'''
    input_id_for_changing_surname = input("Введите id клиента фамилию которого хотите изменить: ")
    input_surname_for_changing = input("Введите фамилию для изменения: ")
    with conn.cursor() as cur:
        cur.execute("""
        UPDATE clients_Homework5 SET client_surname=%s WHERE id=%s;
        """, (input_surname_for_changing, input_id_for_changing_surname))
        conn.commit()

#change_client_surname()



def change_client_email():
    '''Изменение e-mail клиента в таблице clients_Homework5'''
    input_id_for_changing_email = input("Введите id клиента e-mail которого хотите изменить: ")
    input_email_for_changing = input("Введите e-mail для изменения: ")
    with conn.cursor() as cur:
        cur.execute("""
        UPDATE clients_Homework5 SET client_email=%s WHERE id=%s;
        """, (input_email_for_changing, input_id_for_changing_email))
        conn.commit()

#change_client_email()



def change_client_phonenumber():
    '''Изменение номера телефона клиента в таблице client_phonenumbers'''
    input_phonenumber_you_wanna_change = input("Введите номер телефона который Вы хотите изменить: ")
    input_phonenumber_for_changing = input("Введите новый номер телефона, который заменит собой старый: ")
    with conn.cursor() as cur:
        cur.execute("""
        UPDATE client_phonenumbers SET client_phonenumber=%s WHERE client_phonenumber=%s;
        """, (input_phonenumber_for_changing, input_phonenumber_you_wanna_change))
        conn.commit()

#change_client_phonenumber()



def delete_client_phonenumber():
    '''Удаление номера телефона клиента из таблицы client_phonenumbers'''
    input_id_for_deleting_phonenumber = input("Введите id клиента номер телефона которого хотите удалить: ")
    input_phonenumber_for_deleting = input("Введите номер телефона который хотите удалить: ")
    with conn.cursor() as cur:
        cur.execute("""
        DELETE FROM client_phonenumbers WHERE client_id=%s AND client_phonenumber=%s
        """, (input_id_for_deleting_phonenumber, input_phonenumber_for_deleting))
        conn.commit()

#delete_client_phonenumber()



def delete_client():
    '''Удаление имеющейся информации о клиенте'''
    input_id_for_deleting_client = input("Введите id клиента которого хотите удалить: ")
    input_client_surname_for_deleting = input("Введите фамилию клиента которого хотите удалить: ")
    with conn.cursor() as cur:
        #удаление связи с таблицей client_phonenumbers
        cur.execute("""
        DELETE FROM client_phonenumbers WHERE client_id=%s
        """, (input_id_for_deleting_client,))
        #удаление информации о клиенте из таблицы clients_Homework5
        cur.execute("""
        DELETE FROM clients_Homework5 WHERE id=%s AND client_surname=%s
        """, (input_id_for_deleting_client, input_client_surname_for_deleting))
        conn.commit()

#delete_client()



def find_client():
    '''Поиск клиента по имени'''
    input_name_for_finding = input("Введите имя для поиска информации о клиенте: ")
    with conn.cursor() as cur:
        cur.execute("""
        SELECT id, client_surname, client_email, client_phonenumber
        FROM clients_Homework5 AS ch5
        LEFT JOIN client_phonenumbers AS cp ON cp.id_phonenumber = ch5.id
        WHERE client_name=%s
        """, (input_name_for_finding,))
        #return cur.fetchone()[0]
        print(cur.fetchall())

#find_client()



def check_function():
    '''Проверочная функция, отображает содержимое таблиц'''
    with conn.cursor() as cur:
        cur.execute("""
        SELECT * FROM clients_Homework5;
        """)
        pprint(cur.fetchall())
    with conn.cursor() as cur:
        cur.execute("""
        SELECT * FROM client_phonenumbers;
        """)
        pprint(cur.fetchall())

check_function()






def main():
    while True:
        command_symbol = input("\nВведите команду: ")
        if command_symbol == "0":
            create_tables()
        elif command_symbol == "1":
            add_new_client()
        elif command_symbol == "2":
            add_new_phonenumber()
        elif command_symbol == "3":
            change_client_name()
        elif command_symbol == "4":
            change_client_surname()
        elif command_symbol == "5":
            change_client_email()
        elif command_symbol == "6":
            change_client_phonenumber()
        elif command_symbol == "7":
            delete_client_phonenumber()
        elif command_symbol == "8":
            delete_client()
        elif command_symbol == "9":
            find_client()
        else:
            print("\nВы ввели неверный символ, пожалуйста, повторите ввод следуя вышеобозначенным указаниям")

main()

conn.close()