import json
import tkinter as tk
from tkinter import Canvas
import psycopg2
from psycopg2 import Error
import matplotlib.pyplot as plt


def read_db_config(filename="db_config.json"):
    try:
        with open(filename, "r") as file:
            return json.load(file)
    except Exception as e:
        print("Ошибка при чтении конфигурации:", e)
        return None


def connection():
    config = read_db_config()
    if config is None:
        return None

    try:
        conn = psycopg2.connect(**config)
        return conn
    except (Exception, Error) as error:
        print("Ошибка при работе с PostgreSQL", error)
        return None

def disconnection(conn, cursor):
    if conn:
        cursor.close()
        conn.close()


def address():
    M = ''
    m = -1
    conn = connection()
    cursor = conn.cursor()
    query_1 = "select * from dash_address"
    cursor.execute(query_1)
    address_metrix = cursor.fetchall()
    metrix = ['Good', 'Bad']
    values = [0, 0]
    for row in address_metrix:
        if row[0] == 'GOOD' or row[0] == 'POSTAL_BOX':
            values[0] += row[1]
        else:
            values[1] += row[1]
            if max(m, row[1]) > m:
                m = max(m, row[1])
                M = row[0]
    values2 = [0, m]

    plt.figure(figsize=(11, 5))
    plt.subplot(132)
    plt.bar(metrix, values, color=['green', 'red'], edgecolor='black', linewidth=1)
    plt.bar(metrix, values2, color=['green', 'orange'], edgecolor='black', linewidth=1)
    plt.yticks(values)
    plt.ticklabel_format(style='plain', axis='y')
    plt.suptitle('Качество Адрессов')
    plt.xlabel('Самая популярная ошибка с КК - %s' % M)
    plt.ylabel('Колличество')
    plt.show()
    disconnection(conn, cursor)


def inn():
    M = ''
    m = -1
    conn = connection()
    cursor = conn.cursor()
    query_1 = "select * from dash_inn"
    cursor.execute(query_1)
    inn_metrix = cursor.fetchall()
    metrix = ['Good', 'Bad']
    values = [0, 0]
    for row in inn_metrix:
        if row[1] == 'CONFIRMED_MANUALLY' or row[1] == 'GOOD':
            values[0] += row[0]
        else:
            values[1] += row[0]
            if max(m, row[0]) > m:
                m = max(m, row[0])
                M = row[1]
    values2 = [0, m]
    plt.figure(figsize=(11, 5))
    plt.subplot(132)
    plt.bar(metrix, values, color=['green', 'red'], edgecolor='black', linewidth=1)
    plt.bar(metrix, values2, color=['green', 'orange'], edgecolor='black', linewidth=1)
    plt.yticks(values)
    plt.ticklabel_format(style='plain', axis='y')
    plt.suptitle('Качество ИНН')
    plt.xlabel('Самая популярная ошибка с КК - %s' % M)
    plt.ylabel('Колличество')
    plt.show()
    disconnection(conn, cursor)


def fio():
    M = ''
    m = -1
    conn = connection()
    cursor = conn.cursor()
    query_1 = "select * from dash_fio"
    cursor.execute(query_1)
    fio_metrix = cursor.fetchall()
    metrix = ['Good', 'Bad']
    values = [0, 0]
    for row in fio_metrix:
        if row[1] == 'CONFIRMED_MANUALLY' or row[1] == 'EDITED':
            values[0] += row[0]
        else:
            values[1] += row[0]
            if max(m, row[0]) > m:
                m = max(m, row[0])
                M = row[1]
    values2 = [0, m]
    plt.figure(figsize=(11, 5))
    plt.subplot(132)
    plt.bar(metrix, values, color=['green', 'red'], edgecolor='black', linewidth=1)
    plt.bar(metrix, values2, color=['green', 'orange'], edgecolor='black', linewidth=1)
    plt.yticks(values)
    plt.ticklabel_format(style='plain', axis='y')
    plt.suptitle('Качество ФИО')
    plt.xlabel('Самая популярная ошибка с КК - %s' % M)
    plt.ylabel('Колличество')
    plt.show()
    disconnection(conn, cursor)


def snils():
    M = ''
    m = -1
    conn = connection()
    cursor = conn.cursor()
    query_1 = "select * from dash_snils"
    cursor.execute(query_1)
    snils_metrix = cursor.fetchall()
    metrix = ['Correct', 'Bad']
    values = [0, 0]
    for row in snils_metrix:
        if row[1] == 'CONFIRMED_MANUALLY' or row[1] == 'GOOD' or row[1] == 'GOOD_CHANGED':
            values[0] += row[0]
        else:
            values[1] += row[0]
            if max(m, row[0]) > m:
                m = max(m, row[0])
                M = row[1]
    values2 = [0, m]
    plt.figure(figsize=(11, 5))
    plt.subplot(132)
    plt.bar(metrix, values, color=['green', 'red'], edgecolor='black', linewidth=1)
    plt.bar(metrix, values2, color=['green', 'orange'], edgecolor='black', linewidth=1)
    plt.yticks(values)
    plt.ticklabel_format(style='plain', axis='y')
    plt.suptitle('Качество СНИЛС')
    plt.xlabel('Самая популярная ошибка с КК - %s' % M)
    plt.ylabel('Колличество')
    plt.show()
    disconnection(conn, cursor)


def date_of_birth():
    M = ''
    m = -1
    conn = connection()
    cursor = conn.cursor()
    query_1 = "select * from dash_db"
    cursor.execute(query_1)
    db_metrix = cursor.fetchall()
    metrix = ['Good', 'Bad']
    values = [0, 0]
    for row in db_metrix:
        if row[1] == 'CONFIRMED_MANUALLY' or row[1] == 'EDITED':
            values[0] += row[0]
        else:
            values[1] += row[0]
            if max(m, row[0]) > m:
                m = max(m, row[0])
                M = row[1]
    values2 = [0, m]
    plt.figure(figsize=(11, 5))
    plt.subplot(132)
    plt.bar(metrix, values, color=['green', 'red'], edgecolor='black', linewidth=1)
    plt.bar(metrix, values2, color=['green', 'orange'], edgecolor='black', linewidth=1)
    plt.yticks(values)
    plt.ticklabel_format(style='plain', axis='y')
    plt.suptitle('Качество Дат Дня рождения')
    plt.xlabel('Самая популярная ошибка с КК - %s' % M)
    plt.ylabel('Колличество')
    plt.show()
    disconnection(conn, cursor)


def phone():
    conn = connection()
    cursor = conn.cursor()
    query_1 = "select * from dash_phone"
    cursor.execute(query_1)
    phone_metrix = cursor.fetchall()
    metrix = ['Good', 'Doubtful', 'Bad']
    values = [0, 0, 0]
    for row in phone_metrix:
        if row[0] == 'CONFIRMED_MANUALLY' or \
                row[0] == 'GOOD' or \
                row[0] == 'GOOD_REPLACED_CODE' or \
                row[0] == 'GOOD_REPLACED_NUMBER' or \
                row[0] == 'GOOD_REPLACED_CODE_NUMBER':
            values[0] += row[1]
        elif row[0] == 'UNDEF' or row[0] == 'OUT_OF_RANGE':
            values[2] += row[1]
        else:
            values[1] += row[1]
    plt.figure(figsize=(11, 5))
    plt.subplot(132)
    plt.bar(metrix, values, color=['green', 'orange', 'red'], edgecolor='black', linewidth=1)
    plt.yticks(values)
    plt.ticklabel_format(style='plain', axis='y')
    plt.suptitle('Качество Телефонов')
    plt.ylabel('Колличество')
    plt.show()
    disconnection(conn, cursor)


def mail():
    M = ''
    m = -1
    conn = connection()
    cursor = conn.cursor()
    query_1 = "select * from dash_mail"
    cursor.execute(query_1)
    mail_metrix = cursor.fetchall()
    metrix = ['Good', 'Bad']
    values = [0, 0]
    for row in mail_metrix:
        if row[0] == 'CONFIRMED_MANUALLY' or row[0] == 'GOOD':
            values[0] += row[1]
        else:
            values[1] += row[1]
            if max(m, row[1]) > m:
                m = max(m, row[1])
                M = row[0]
    values2 = [0, m]
    plt.figure(figsize=(11, 5))
    plt.subplot(132)
    plt.bar(metrix, values, color=['green', 'red'], edgecolor='black', linewidth=1)
    plt.bar(metrix, values2, color=['green', 'orange'], edgecolor='black', linewidth=1)
    plt.yticks(values)
    plt.ticklabel_format(style='plain', axis='y')
    plt.suptitle('Качество Почты')
    plt.xlabel('Самая популярная ошибка с КК - %s' % M)
    plt.ylabel('Колличество')
    plt.show()
    disconnection(conn, cursor)


def sourses():
    conn = connection()
    cursor = conn.cursor()
    values_good = [0, 0, 0]
    values_bad = [0, 0, 0]

    query1 = 'select * from dash_address_istoch_good'
    query2 = 'select * from dash_address_istoch_bad'
    query3 = 'select * from dash_fio_istoch_good'
    query4 = 'select * from dash_fio_istoch_bad'
    query5 = 'select * from dash_inn_istoch_good'
    query6 = 'select * from dash_inn_istoch_bad'
    query7 = 'select * from dash_mail_istoch_good'
    query8 = 'select * from dash_mail_istoch_bad'
    query9 = 'select * from dash_phone_istoch_good'
    query10 = 'select * from dash_phone_istoch_bad'
    query11 = 'select * from dash_snils_istoch_good'
    query12 = 'select * from dash_snils_istoch_bad'
    cursor.execute(query1)
    address_istoch_good = cursor.fetchall()
    for row in address_istoch_good:
        if row[0] == 'AL':
            values_good[0] += row[1]
        if row[0] == 'BT':
            values_good[1] += row[1]
        if row[0] == 'GM':
            values_good[2] += row[1]
    cursor.execute(query2)
    address_istoch_bad = cursor.fetchall()
    for row in address_istoch_bad:
        if row[0] == 'AL':
            values_bad[0] += row[1]
        if row[0] == 'BT':
            values_bad[1] += row[1]
        if row[0] == 'GM':
            values_bad[2] += row[1]
    cursor.execute(query3)
    fio_istoch_good = cursor.fetchall()
    for row in fio_istoch_good:
        if row[0] == 'AL':
            values_good[0] += row[1]
        if row[0] == 'BT':
            values_good[1] += row[1]
        if row[0] == 'GM':
            values_good[2] += row[1]
    cursor.execute(query4)
    fio_istoch_bad = cursor.fetchall()
    for row in fio_istoch_bad:
        if row[0] == 'AL':
            values_bad[0] += row[1]
        if row[0] == 'BT':
            values_bad[1] += row[1]
        if row[0] == 'GM':
            values_bad[2] += row[1]
    cursor.execute(query5)
    inn_istoch_good = cursor.fetchall()
    for row in inn_istoch_good:
        if row[0] == 'AL':
            values_good[0] += row[1]
        if row[0] == 'BT':
            values_good[1] += row[1]
        if row[0] == 'GM':
            values_good[2] += row[1]
    cursor.execute(query6)
    inn_istoch_bad = cursor.fetchall()
    for row in inn_istoch_bad:
        if row[0] == 'AL':
            values_bad[0] += row[1]
        if row[0] == 'BT':
            values_bad[1] += row[1]
        if row[0] == 'GM':
            values_bad[2] += row[1]
    cursor.execute(query7)
    mail_istoch_good = cursor.fetchall()
    for row in mail_istoch_good:
        if row[0] == 'AL':
            values_good[0] += row[1]
        if row[0] == 'BT':
            values_good[1] += row[1]
        if row[0] == 'GM':
            values_good[2] += row[1]
    cursor.execute(query8)
    mail_istoch_bad = cursor.fetchall()
    for row in mail_istoch_bad:
        if row[0] == 'AL':
            values_bad[0] += row[1]
        if row[0] == 'BT':
            values_bad[1] += row[1]
        if row[0] == 'GM':
            values_bad[2] += row[1]
    cursor.execute(query9)
    phone_istoch_good = cursor.fetchall()
    for row in phone_istoch_good:
        if row[0] == 'AL':
            values_good[0] += row[1]
        if row[0] == 'BT':
            values_good[1] += row[1]
        if row[0] == 'GM':
            values_good[2] += row[1]
    cursor.execute(query10)
    phone_istoch_bad = cursor.fetchall()
    for row in phone_istoch_bad:
        if row[0] == 'AL':
            values_bad[0] += row[1]
        if row[0] == 'BT':
            values_bad[1] += row[1]
        if row[0] == 'GM':
            values_bad[2] += row[1]
    cursor.execute(query11)
    snils_istoch_good = cursor.fetchall()
    for row in snils_istoch_good:
        if row[0] == 'AL':
            values_good[0] += row[1]
        if row[0] == 'BT':
            values_good[1] += row[1]
        if row[0] == 'GM':
            values_good[2] += row[1]
    cursor.execute(query12)
    snils_istoch_bad = cursor.fetchall()
    for row in snils_istoch_bad:
        if row[0] == 'AL':
            values_bad[0] += row[1]
        if row[0] == 'BT':
            values_bad[1] += row[1]
        if row[0] == 'GM':
            values_bad[2] += row[1]

    percents_good = [round(values_good[0] * 100 / (values_good[0] + values_bad[0])),
                     round(values_good[1] * 100 / (values_good[1] + values_bad[1])),
                     round(values_good[2] * 100 / (values_good[2] + values_bad[2]))]
    percents_bad = [round(values_bad[0] * 100 / (values_good[0] + values_bad[0])),
                    round(values_bad[1] * 100 / (values_good[1] + values_bad[1])),
                    round(values_bad[2] * 100 / (values_good[2] + values_bad[2]))]

    plt.figure(figsize=(11, 5))
    plt.subplot(1, 3, 1)
    plt.pie([percents_good[0], percents_bad[0]], labels=['Грязные', 'Качественные'], colors=['red', 'green'],
            autopct='%.0f', explode=(0, 0.2), shadow=True)
    plt.title('Данные от Альфы')

    plt.subplot(1, 3, 2)
    plt.pie([percents_good[1], percents_bad[1]], labels=['Грязные', 'Качественные'], colors=['red', 'green'],
            autopct='%.0f', explode=(0, 0.2), shadow=True)
    plt.title('Данные от Бетты')

    plt.subplot(1, 3, 3)
    plt.pie([percents_good[2], percents_bad[2]], labels=['Грязные', 'Качественные'], colors=['red', 'green'],
            autopct='%.0f', explode=(0, 0.2), shadow=True)
    plt.title('Данные от Гаммы')

    plt.suptitle('Анализ источников')
    plt.show()
    disconnection(conn, cursor)


def phone_rt():
    conn = connection()
    cursor = conn.cursor()
    cursor.execute("select p.qualitycode, count(*) into _newera_phone_testpY_0 from physical_party pp "
                   "join phone p on pp.hid_party = p.hid_party where (pp.merged_status in (0,2) "
                   "and pp.enddate is null) "
                   "and (p.enddate is null) group by p.qualitycode ")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM _newera_phone_testpY_0")
    phone_metrix = cursor.fetchall()
    metrix = ['Correct', 'Doubtful', 'Bad']
    values = [0, 0, 0]
    for row in phone_metrix:
        if row[0] == 'GOOD':
            values[0] += row[1]
        elif 'GOOD' in row[0]:
            values[1] += row[1]
        else:
            values[2] += row[1]
    plt.figure(figsize=(11, 5))
    plt.subplot(132)
    plt.bar(metrix, values, color=['green', 'orange', 'red'], edgecolor='black', linewidth=1)
    plt.yticks(values)
    plt.ticklabel_format(style='plain', axis='y')
    plt.suptitle('Качество Телефонов')
    plt.ylabel('Колличество')
    plt.show()
    disconnection(conn, cursor)


def fio_rt():
    M = ''
    m = -1
    conn = connection()
    cursor = conn.cursor()
    cursor.execute("SELECT count(*), pp.fullname_qc from physical_party as pp "
                   "where (pp.merged_status in (0,2) and pp.enddate is null) group by  pp.fullname_qc")
    fio_metrix = cursor.fetchall()
    metrix = ['Good', 'Bad']
    values = [0, 0]
    for row in fio_metrix:
        if row[1] == 'CONFIRMED_MANUALLY' or row[1] == 'EDITED':
            values[0] += row[0]
        else:
            values[1] += row[0]
            if max(m, row[0]) > m:
                m = max(m, row[0])
                M = row[1]
    values2 = [0, m]
    plt.figure(figsize=(11, 5))
    plt.subplot(132)
    plt.bar(metrix, values, color=['green', 'red'], edgecolor='black', linewidth=1)
    plt.bar(metrix, values2, color=['green', 'orange'], edgecolor='black', linewidth=1)
    plt.yticks(values)
    plt.ticklabel_format(style='plain', axis='y')
    plt.suptitle('Качество ФИО')
    plt.xlabel('Самая популярная ошибка с КК - %s' % M)
    plt.ylabel('Колличество')
    plt.show()
    disconnection(conn, cursor)


def fio_index():
    conn = connection()
    cursor = conn.cursor()
    cursor.execute("CREATE INDEX for_FIO_index ON physical_party (fullname_qc,merged_status,enddate)")
    conn.commit()
    disconnection(conn, cursor)


def date_of_birth_index():
    conn = connection()
    cursor = conn.cursor()
    cursor.execute("CREATE INDEX for_DR_index ON physical_party (birthdate_qc,merged_status,enddate)")
    conn.commit()
    disconnection(conn, cursor)


def date_of_birth_rt():
    M = ''
    m = -1
    conn = connection()
    cursor = conn.cursor()
    cursor.execute("SELECT count(*), pp.birthdate_qc from physical_party as pp "
                   "where (pp.merged_status in (0,2) and pp.enddate is null) group by  pp.birthdate_qc")
    db_metrix = cursor.fetchall()
    metrix = ['Good', 'Bad']
    values = [0, 0]
    for row in db_metrix:
        if row[1] == 'CONFIRMED_MANUALLY' or row[1] == 'EDITED':
            values[0] += row[0]
        else:
            values[1] += row[0]
            if max(m, row[0]) > m:
                m = max(m, row[0])
                M = row[1]
    values2 = [0, m]
    plt.figure(figsize=(11, 5))
    plt.subplot(132)
    plt.bar(metrix, values, color=['green', 'red'], edgecolor='black', linewidth=1)
    plt.bar(metrix, values2, color=['green', 'orange'], edgecolor='black', linewidth=1)
    plt.yticks(values)
    plt.ticklabel_format(style='plain', axis='y')
    plt.suptitle('Качество Дат Дня рождения')
    plt.xlabel('Самая популярная ошибка с КК - %s' % M)
    plt.ylabel('Колличество')
    plt.show()
    disconnection(conn, cursor)


def inn_index():
    conn = connection()
    cursor = conn.cursor()
    cursor.execute("CREATE INDEX for_INN_index ON physical_party (inn_qc,merged_status,enddate)")
    conn.commit()
    disconnection(conn, cursor)


def inn_rt():
    M = ''
    m = -1
    conn = connection()
    cursor = conn.cursor()
    cursor.execute("SELECT count(*), pp.inn_qc from physical_party as pp "
                   "where (pp.merged_status in (0,2) and pp.enddate is null) group by  pp.inn_qc")
    inn_metrix = cursor.fetchall()
    metrix = ['Good', 'Bad']
    values = [0, 0]
    for row in inn_metrix:
        if row[1] == 'CONFIRMED_MANUALLY' or row[1] == 'GOOD':
            values[0] += row[0]
        else:
            values[1] += row[0]
            if max(m, row[0]) > m:
                m = max(m, row[0])
                M = row[1]
    values2 = [0, m]
    plt.figure(figsize=(11, 5))
    plt.subplot(132)
    plt.bar(metrix, values, color=['green', 'red'], edgecolor='black', linewidth=1)
    plt.bar(metrix, values2, color=['green', 'orange'], edgecolor='black', linewidth=1)
    plt.yticks(values)
    plt.ticklabel_format(style='plain', axis='y')
    plt.suptitle('Качество ИНН')
    plt.xlabel('Самая популярная ошибка с КК - %s' % M)
    plt.ylabel('Колличество')
    plt.show()
    disconnection(conn, cursor)


def snils_index():
    conn = connection()
    cursor = conn.cursor()
    cursor.execute("CREATE INDEX for_SNILS_index ON physical_party (snils_qc,merged_status,enddate)")
    conn.commit()
    disconnection(conn, cursor)


def snils_rt():
    M = ''
    m = -1
    conn = connection()
    cursor = conn.cursor()
    cursor.execute("SELECT count(*), pp.snils_qc from physical_party as pp "
                   "where (pp.merged_status in (0,2) and pp.enddate is null) group by  pp.snils_qc")
    snils_metrix = cursor.fetchall()
    metrix = ['Correct', 'Bad']
    values = [0, 0]
    for row in snils_metrix:
        if row[1] == 'CONFIRMED_MANUALLY' or row[1] == 'GOOD' or row[1] == 'GOOD_CHANGED':
            values[0] += row[0]
        else:
            values[1] += row[0]
            if max(m, row[0]) > m:
                m = max(m, row[0])
                M = row[1]
    values2 = [0, m]
    plt.figure(figsize=(11, 5))
    plt.subplot(132)
    plt.bar(metrix, values, color=['green', 'red'], edgecolor='black', linewidth=1)
    plt.bar(metrix, values2, color=['green', 'orange'], edgecolor='black', linewidth=1)
    plt.yticks(values)
    plt.ticklabel_format(style='plain', axis='y')
    plt.suptitle('Качество СНИЛС')
    plt.xlabel('Самая популярная ошибка с КК - %s' % M)
    plt.ylabel('Колличество')
    plt.show()
    disconnection(conn, cursor)


def email_rt():
    M = ''
    m = -1
    conn = connection()
    cursor = conn.cursor()
    cursor.execute("select p.qualitycode, count(*) into _newera_email_testpY from physical_party pp "
                   "join email p on pp.hid_party = p.hid_party where (pp.merged_status in (0,2) and pp.enddate is null)"
                   "and (p.enddate is null) group by p.qualitycode")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM _newera_email_testpY")
    mail_metrix = cursor.fetchall()
    metrix = ['Good', 'Bad']
    values = [0, 0]
    for row in mail_metrix:
        if row[0] == 'CONFIRMED_MANUALLY' or row[0] == 'GOOD':
            values[0] += row[1]
        else:
            values[1] += row[1]
            if max(m, row[1]) > m:
                m = max(m, row[1])
                M = row[0]
    values2 = [0, m]
    plt.figure(figsize=(11, 5))
    plt.subplot(132)
    plt.bar(metrix, values, color=['green', 'red'], edgecolor='black', linewidth=1)
    plt.bar(metrix, values2, color=['green', 'orange'], edgecolor='black', linewidth=1)
    plt.yticks(values)
    plt.ticklabel_format(style='plain', axis='y')
    plt.suptitle('Качество Почты')
    plt.xlabel('Самая популярная ошибка с КК - %s' % M)
    plt.ylabel('Колличество')
    plt.show()
    disconnection(conn, cursor)


def address_rt():
    M = ''
    m = -1
    conn = connection()
    cursor = conn.cursor()
    cursor.execute("select p.qualitycode, count(*) into _newera_address_testpY from physical_party pp "
                   "join address p on pp.hid_party = p.hid_party"
                   " where (pp.merged_status in (0,2) and pp.enddate is null)"
                   "and (p.enddate_adress is null) group by p.qualitycode")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM _newera_address_testpY")
    address_metrix = cursor.fetchall()
    metrix = ['Good', 'Bad']
    values = [0, 0]
    for row in address_metrix:
        if row[0] == 'GOOD' or row[0] == 'POSTAL_BOX':
            values[0] += row[1]
        else:
            values[1] += row[1]
            if max(m, row[1]) > m:
                m = max(m, row[1])
                M = row[0]
    values2 = [0, m]

    plt.figure(figsize=(11, 5))
    plt.subplot(132)
    plt.bar(metrix, values, color=['green', 'red'], edgecolor='black', linewidth=1)
    plt.bar(metrix, values2, color=['green', 'orange'], edgecolor='black', linewidth=1)
    plt.yticks(values)
    plt.ticklabel_format(style='plain', axis='y')
    plt.suptitle('Качество Адрессов')
    plt.xlabel('Самая популярная ошибка с КК - %s' % M)
    plt.ylabel('Колличество')
    plt.show()
    disconnection(conn, cursor)


def document():
    M = ''
    m = -1
    conn = connection()
    cursor = conn.cursor()
    query_1 = "select * from _dash_newera_Document_testpY"
    cursor.execute(query_1)
    doc_metrix = cursor.fetchall()
    metrix = ['Good', 'Bad']
    values = [0, 0]
    for row in doc_metrix:
        if row[0] == 'EDITED' or \
           row[0] == 'CONFIRMED_MANUALLY' or \
           row[0] == 'EDITED_NOT_CHECK' or \
           row[0] == 'EDITED_PARTIAL_REQ':
            values[0] += row[1]
        else:
            values[1] += row[1]
            if max(m, row[1]) > m:
                m = max(m, row[1])
                M = row[0]
    values2 = [0, m]

    plt.figure(figsize=(11, 5))
    plt.subplot(132)
    plt.bar(metrix, values, color=['green', 'red'])
    plt.bar(metrix, values2, color=['green', 'orange'], edgecolor='black', linewidth=1)
    plt.xlabel('Самая популярная ошибка с КК - %s' % M)
    plt.yticks(values)
    plt.ticklabel_format(style='plain', axis='y')
    plt.suptitle('quality Document')
    plt.show()
    disconnection(conn, cursor)


def document_rt():
    M = ''
    m = -1
    conn = connection()
    cursor = conn.cursor()
    cursor.execute("select p.qualitycode, count(*) into dash_Document from physical_party pp "
                   "join Document p on pp.hid_party = p.hid_party"
                   " where (pp.merged_status in (0,2) and pp.enddate is null) "
                   "and (p.enddate is null) group by p.qualitycode")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM dash_Document")
    doc_metrix = cursor.fetchall()
    metrix = ['Good', 'Bad']
    values = [0, 0]
    for row in doc_metrix:
        if row[0] == 'EDITED' or \
                row[0] == 'CONFIRMED_MANUALLY' or \
                row[0] == 'EDITED_NOT_CHECK' or \
                row[0] == 'EDITED_PARTIAL_REQ':
            values[0] += row[1]
        else:
            values[1] += row[1]
            if max(m, row[1]) > m:
                m = max(m, row[1])
                M = row[0]
    values2 = [0, m]

    plt.figure(figsize=(11, 5))
    plt.subplot(132)
    plt.bar(metrix, values, color=['green', 'red'])
    plt.bar(metrix, values2, color=['green', 'orange'], edgecolor='black', linewidth=1)
    plt.xlabel('Самая популярная ошибка с КК - %s' % M)
    plt.yticks(values)
    plt.ticklabel_format(style='plain', axis='y')
    plt.suptitle('quality Document')
    plt.show()
    disconnection(conn, cursor)


def sourses_rt():
    conn = connection()
    cursor = conn.cursor()

    values_good = [0, 0, 0]
    values_bad = [0, 0, 0]

    cursor.execute(
        "select p1.name, count(*) into GG_1 from system p1 join phone p2 on p1.name=(substring(p2.author,1,2)) and "
        "p2.qualitycode='GOOD' group by p1.name")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM GG_1")
    address_istoch_good = cursor.fetchall()
    for row in address_istoch_good:
        if row[0] == 'AL':
            values_good[0] += row[1]
        if row[0] == 'BT':
            values_good[1] += row[1]
        if row[0] == 'GM':
            values_good[2] += row[1]

    cursor.execute(
        "select p1.name, count(*) into GG_2 from system p1 join phone p2 on p1.name=(substring(p2.author,1,2)) "
        "and p2.qualitycode!='GOOD' group by p1.name")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM GG_2")
    address_istoch_bad = cursor.fetchall()
    for row in address_istoch_bad:
        if row[0] == 'AL':
            values_bad[0] += row[1]
        if row[0] == 'BT':
            values_bad[1] += row[1]
        if row[0] == 'GM':
            values_bad[2] += row[1]

    cursor.execute("select p1.name, count(*) into GG_3 from system p1 join physical_party p2 on p1.name=(substring"
                   "(p2.fullname_author,1,2)) and (p2.fullname_qc='EDITED' or p2.fullname_qc='CONFIRMED_MANUALLY') "
                   "group by p1.name")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM GG_3")
    fio_istoch_good = cursor.fetchall()
    for row in fio_istoch_good:
        if row[0] == 'AL':
            values_good[0] += row[1]
        if row[0] == 'BT':
            values_good[1] += row[1]
        if row[0] == 'GM':
            values_good[2] += row[1]

    cursor.execute("select p1.name, count(*) into GG_4 from system p1 join physical_party p2 on "
                   "p1.name=(substring(p2.fullname_author,1,2)) and (p2.fullname_qc!='EDITED' "
                   "and p2.fullname_qc!='CONFIRMED_MANUALLY') group by p1.name")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM GG_4")
    fio_istoch_bad = cursor.fetchall()
    for row in fio_istoch_bad:
        if row[0] == 'AL':
            values_bad[0] += row[1]
        if row[0] == 'BT':
            values_bad[1] += row[1]
        if row[0] == 'GM':
            values_bad[2] += row[1]

    cursor.execute("select p1.name, count(*) into GG_5 from system p1 join physical_party p2 on "
                   "p1.name=(substring(p2.inn_author,1,2)) and p2.inn_qc ='GOOD' group by p1.name")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM GG_5")
    inn_istoch_good = cursor.fetchall()
    for row in inn_istoch_good:
        if row[0] == 'AL':
            values_good[0] += row[1]
        if row[0] == 'BT':
            values_good[1] += row[1]
        if row[0] == 'GM':
            values_good[2] += row[1]

    cursor.execute("select p1.name, count(*) into GG_6 from system p1 join physical_party p2 on "
                   "p1.name=(substring(p2.inn_author,1,2)) and p2. inn_qc!='GOOD' group by p1.name")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM GG_6")
    inn_istoch_bad = cursor.fetchall()
    for row in inn_istoch_bad:
        if row[0] == 'AL':
            values_bad[0] += row[1]
        if row[0] == 'BT':
            values_bad[1] += row[1]
        if row[0] == 'GM':
            values_bad[2] += row[1]

    cursor.execute(
        "select p1.name, count(*) into GG_7 from system p1 join email p2 on p1.name=(substring(p2.author,1,2)) "
        "and p2.qualitycode='GOOD' group by p1.name")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM GG_7")
    mail_istoch_good = cursor.fetchall()
    for row in mail_istoch_good:
        if row[0] == 'AL':
            values_good[0] += row[1]
        if row[0] == 'BT':
            values_good[1] += row[1]
        if row[0] == 'GM':
            values_good[2] += row[1]

    cursor.execute("select p1.name, count(*) into GG_8 from system p1 join email p2 "
                   "on p1.name=(substring(p2.author,1,2)) "
                   "and p2.qualitycode!='GOOD' group by p1.name")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM GG_8")
    mail_istoch_bad = cursor.fetchall()
    for row in mail_istoch_bad:
        if row[0] == 'AL':
            values_bad[0] += row[1]
        if row[0] == 'BT':
            values_bad[1] += row[1]
        if row[0] == 'GM':
            values_bad[2] += row[1]

    cursor.execute(
        "select p1.name, count(*) into GG_9 from system p1 join phone p2 on p1.name=(substring(p2.author,1,2)) "
        "and p2.qualitycode='GOOD' group by p1.name")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM GG_9")
    phone_istoch_good = cursor.fetchall()
    for row in phone_istoch_good:
        if row[0] == 'AL':
            values_good[0] += row[1]
        if row[0] == 'BT':
            values_good[1] += row[1]
        if row[0] == 'GM':
            values_good[2] += row[1]

    cursor.execute(
        "select p1.name, count(*) into GG_10 from system p1 join phone p2 on p1.name=(substring(p2.author,1,2)) "
        "and p2.qualitycode!='GOOD' group by p1.name")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM GG_10")
    phone_istoch_bad = cursor.fetchall()
    for row in phone_istoch_bad:
        if row[0] == 'AL':
            values_bad[0] += row[1]
        if row[0] == 'BT':
            values_bad[1] += row[1]
        if row[0] == 'GM':
            values_bad[2] += row[1]

    cursor.execute("select p1.name, count(*) into GG_11 from system p1 join physical_party p2 "
                   "on p1.name=(substring(p2.snils_author,1,2)) and p2.snils_qc='GOOD' group by p1.name")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM GG_11")
    snils_istoch_good = cursor.fetchall()
    for row in snils_istoch_good:
        if row[0] == 'AL':
            values_good[0] += row[1]
        if row[0] == 'BT':
            values_good[1] += row[1]
        if row[0] == 'GM':
            values_good[2] += row[1]

    cursor.execute("select p1.name, count(*) into GG_12 from system p1 join physical_party p2 "
                   "on p1.name=(substring(p2.snils_author,1,2)) and p2.snils_qc!='GOOD' group by p1.name")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM GG_12")
    snils_istoch_bad = cursor.fetchall()
    for row in snils_istoch_bad:
        if row[0] == 'AL':
            values_bad[0] += row[1]
        if row[0] == 'BT':
            values_bad[1] += row[1]
        if row[0] == 'GM':
            values_bad[2] += row[1]

    cursor.execute("select p1.name, count(*) into GG_13 from system p1 join Document p2 "
                   "on p1.name=(substring(p2.author,1,2)) and (p2.qualitycode='EDITED' "
                   "or p2.qualitycode  ='CONFIRMED_MANUALLY') group by p1.name")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM GG_13")
    document_istoch_good = cursor.fetchall()
    for row in document_istoch_good:
        if row[0] == 'AL':
            values_good[0] += row[1]
        if row[0] == 'BT':
            values_good[1] += row[1]
        if row[0] == 'GM':
            values_good[2] += row[1]

    cursor.execute("select p1.name, count(*) into GG_14 from system p1 join Document p2 "
                   "on p1.name=(substring(p2.author,1,2)) and (p2.qualitycode != 'EDITED' "
                   "or p2.qualitycode  !='CONFIRMED_MANUALLY') group by p1.name")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM GG_14")
    document_istoch_bad = cursor.fetchall()
    for row in document_istoch_bad:
        if row[0] == 'AL':
            values_bad[0] += row[1]
        if row[0] == 'BT':
            values_bad[1] += row[1]
        if row[0] == 'GM':
            values_bad[2] += row[1]

    percents_good = [round(values_good[0] * 100 / (values_good[0] + values_bad[0])),
                     round(values_good[1] * 100 / (values_good[1] + values_bad[1])),
                     round(values_good[2] * 100 / (values_good[2] + values_bad[2]))]
    percents_bad = [round(values_bad[0] * 100 / (values_good[0] + values_bad[0])),
                    round(values_bad[1] * 100 / (values_good[1] + values_bad[1])),
                    round(values_bad[2] * 100 / (values_good[2] + values_bad[2]))]

    plt.figure(figsize=(11, 5))
    plt.subplot(1, 3, 1)
    plt.pie([percents_good[0], percents_bad[0]], labels=['Грязные', 'Качественные'], colors=['red', 'green'],
            autopct='%.0f', explode=(0, 0.2), shadow=True)
    plt.title('Данные от Альфы')

    plt.subplot(1, 3, 2)
    plt.pie([percents_good[1], percents_bad[1]], labels=['Грязные', 'Качественные'], colors=['red', 'green'],
            autopct='%.0f', explode=(0, 0.2), shadow=True)
    plt.title('Данные от Бетты')

    plt.subplot(1, 3, 3)
    plt.pie([percents_good[2], percents_bad[2]], labels=['Грязные', 'Качественные'], colors=['red', 'green'],
            autopct='%.0f', explode=(0, 0.2), shadow=True)
    plt.title('Данные от Гаммы')

    plt.suptitle('Анализ источников')
    plt.show()
    disconnection(conn, cursor)


def window():
    win = tk.Tk()
    win.title('Анализ базы')
    win.geometry('700x500+300+100')
    canvas = Canvas(win, width=700, height=500)
    canvas.create_line(240, 0, 240, 500, dash=(4, 2), width=3, fill="gray")
    canvas.place(x=0, y=0)

    tk.Button(win, text='Качество ФИО', command=fio).grid(row=1, column=1, stick='we')
    tk.Button(win, text='Качество даты рождения', command=date_of_birth).grid(row=3, column=1, stick='we')
    tk.Button(win, text='Качество ИНН', command=inn).grid(row=5, column=1, stick='we')
    tk.Button(win, text='Качество СНИЛС', command=snils).grid(row=7, column=1, stick='we')
    tk.Button(win, text='Качество адресов', command=address).grid(row=9, column=1, stick='we')
    tk.Button(win, text='Качество телефонов', command=phone).grid(row=11, column=1, stick='we')
    tk.Button(win, text='Качество email', command=mail).grid(row=13, column=1, stick='we')
    tk.Button(win, text='Качество паспортов', command=document).grid(row=15, column=1, stick='we')
    tk.Button(win, text='Анализ источников', command=sourses, background='#bbbbbb').grid(row=17, column=1, stick='we')

    tk.Button(win, text='Качество ФИО', command=fio_rt).grid(row=1, column=3, stick='we')
    tk.Button(win, text='Качество даты рождения', command=date_of_birth_rt).grid(row=3, column=3, stick='we')
    tk.Button(win, text='Качество ИНН', command=inn_rt).grid(row=5, column=3, stick='we')
    tk.Button(win, text='Качество СНИЛС', command=snils_rt).grid(row=7, column=3, stick='we')
    tk.Button(win, text='Качество адресов', command=address_rt).grid(row=9, column=3, stick='we')
    tk.Button(win, text='Качество телефонов', command=phone_rt).grid(row=11, column=3, stick='we')
    tk.Button(win, text='Качество email', command=email_rt).grid(row=13, column=3, stick='we')
    tk.Button(win, text='Качество паспортов', command=document_rt).grid(row=15, column=3, stick='we')
    tk.Button(win, text='Анализ источников', command=sourses_rt, background='#bbbbbb').grid(row=17, column=3, stick='we')

    tk.Button(win, text='индексировать', command=fio_index).grid(row=1, column=5, stick='we')
    tk.Button(win, text='индексировать', command=date_of_birth_index).grid(row=3, column=5, stick='we')
    tk.Button(win, text='индексировать', command=inn_index).grid(row=5, column=5, stick='we')
    tk.Button(win, text='индексировать', command=snils_index).grid(row=7, column=5, stick='we')

    tk.Label(win, text='Сохраненные данные').grid(row=0, column=1, stick='we')
    tk.Label(win, text='Текущее состояние').grid(row=0, column=3, stick='we')

    win.grid_rowconfigure(0, minsize=40)
    win.grid_rowconfigure(2, minsize=20)
    win.grid_rowconfigure(4, minsize=20)
    win.grid_rowconfigure(6, minsize=20)
    win.grid_rowconfigure(8, minsize=20)
    win.grid_rowconfigure(10, minsize=20)
    win.grid_rowconfigure(12, minsize=20)
    win.grid_rowconfigure(14, minsize=20)
    win.grid_rowconfigure(16, minsize=20)
    win.grid_columnconfigure(0, minsize=60)
    win.grid_columnconfigure(1, minsize=130)
    win.grid_columnconfigure(2, minsize=60)
    win.grid_columnconfigure(3, minsize=130)
    win.grid_columnconfigure(4, minsize=20)
    win.grid_columnconfigure(5, minsize=80)



    win.mainloop()


window()
