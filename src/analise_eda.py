# Auto-generated from notebooks/Notebook_Evelyn.ipynb

# %% Cell 0
from pathlib import Path

BASE_DIR = Path.cwd()
if (BASE_DIR / "data").exists():
    DATA_DIR = BASE_DIR / "data"
elif (BASE_DIR.parent / "data").exists():
    DATA_DIR = BASE_DIR.parent / "data"
else:
    DATA_DIR = BASE_DIR / "data"

import pandas as pd
import matplotlib.pyplot as plt

# Formata valores numericos com duas casas decimais no pandas.
pd.set_option("display.float_format", "{:,.2f}".format)

# %% Cell 1
df1 = pd.read_csv(DATA_DIR / "query_01.csv")
df2 = pd.read_csv(DATA_DIR / "query_02.csv")

# %% Cell 2
df1.head()

# %% Cell 3
df2.head()

# %% Cell 4
df1.info()

# %% Cell 5
df2.info()

# %% Cell 6
df1.describe()

# %% Cell 7
df2.describe(include="all")

# %% Cell 8
df1.isnull().sum()

# %% Cell 9
df2.isnull().sum()

# %% Cell 10
print("Média:", df1["SALARY"].mean())
print("Mediana:", df1["SALARY"].median())
print("Mínimo:", df1["SALARY"].min())
print("Máximo:", df1["SALARY"].max())

# %% Cell 11
plt.figure(figsize=(8,5))
plt.hist(df1["SALARY"], bins=10, edgecolor="black")
plt.title("Distribuição dos Salários")
plt.xlabel("Salário")
plt.ylabel("Quantidade de Funcionários")
plt.show()

# %% Cell 12
df1.groupby("DEPARTMENT_NAME")["SALARY"].mean().sort_values(ascending=False)

# %% Cell 13
media_cargo = (
    df1.groupby("JOB_TITLE")["SALARY"]
    .mean()
    .sort_values(ascending=False)
    .head(10)
)
media_cargo

# %% Cell 14
media_cargo.sort_values().plot(kind="barh", figsize=(9,5))
plt.title("Top 10 Cargos com Maior Média Salarial")
plt.xlabel("Salário Médio")
plt.ylabel("Cargo")
plt.show()

# %% Cell 15
plt.figure(figsize=(12,6))
df1.boxplot(column="SALARY", by="DEPARTMENT_NAME", rot=90)
plt.title("Salário por Departamento")
plt.suptitle("")
plt.xlabel("Departamento")
plt.ylabel("Salário")
plt.show()

# %% Cell 16
cargo = (
    df1.groupby("JOB_TITLE")["SALARY"]
    .mean()
    .sort_values()
)
plt.figure(figsize=(10,8))
cargo.plot(kind="barh")
plt.title("Média Salarial por Cargo")
plt.xlabel("Salário Médio")
plt.ylabel("Cargo")
plt.show()

# %% Cell 17
df.shape
#explicação dos 106 registros

# %% Cell 18
df = pd.merge(
    df1,
    df2[["EMPLOYEE_ID", "REGION_NAME"]],
    on="EMPLOYEE_ID"
)

# %% Cell 19
df.shape

# %% Cell 20
df1.shape, df2.shape, df.shape

# %% Cell 21
df.groupby("REGION_NAME")["SALARY"].mean()

# %% Cell 22
df.groupby("REGION_NAME")["SALARY"].mean().plot(
    kind="bar",
    figsize=(7,4)
)
plt.title("Média Salarial por Região")
plt.xlabel("Região")
plt.ylabel("Salário Médio")
plt.show()

# %% Cell 23
func_por_depto = df1["DEPARTMENT_NAME"].value_counts()
func_por_depto

# %% Cell 24
func_por_depto.sort_values().plot(kind="barh", figsize=(8,5))
plt.title("Quantidade de Funcionários por Departamento")
plt.xlabel("Quantidade de Funcionários")
plt.ylabel("Departamento")
plt.show()

# %% Cell 25
resumo_departamento = df1.groupby("DEPARTMENT_NAME").agg(
    MEDIA_SALARIAL=("SALARY", "mean"),
    QTD_FUNCIONARIOS=("EMPLOYEE_ID", "count")
).sort_values("MEDIA_SALARIAL", ascending=False)
resumo_departamento

# %% Cell 26
faixas = pd.cut(
    df1["SALARY"],
    bins=[0,4000,7000,10000,25000],
    labels=[
        "Até R$4.000",
        "R$4.001–7.000",
        "R$7.001–10.000",
        "Acima de R$10.000"
    ]
)
faixas.value_counts().sort_index().plot(
    kind="bar",
    figsize=(8,4)
)
plt.title("Distribuição dos Funcionários por Faixa Salarial")
plt.xlabel("Faixa Salarial")
plt.ylabel("Quantidade")
plt.show()

# %% Cell 27
Q1 = df1["SALARY"].quantile(0.25)
Q3 = df1["SALARY"].quantile(0.75)
IQR = Q3 - Q1
outliers = df1[
    (df1["SALARY"] < Q1 - 1.5 * IQR) |
    (df1["SALARY"] > Q3 + 1.5 * IQR)
]
outliers

# %% Cell 28
"""
# QUERY 1: Funcionários, cargos e departamentos
SELECT
    e.employee_id,
    e.first_name,
    e.last_name,
    e.salary,
    j.job_title,
    d.department_name
FROM hr.employees e
LEFT JOIN hr.jobs j
    ON e.job_id = j.job_id
LEFT JOIN hr.departments d
    ON e.department_id = d.department_id
WHERE e.salary IS NOT NULL
ORDER BY e.salary DESC;
"""

# %% Cell 29
"""
# QUERY 2: Funcionários, departamentos e localização
SELECT
    e.employee_id,
    e.first_name,
    e.last_name,
    d.department_name,
    l.city,
    c.country_name,
    r.region_name
FROM hr.employees e
LEFT JOIN hr.departments d
    ON e.department_id = d.department_id
LEFT JOIN hr.locations l
    ON d.location_id = l.location_id
LEFT JOIN hr.countries c
    ON l.country_id = c.country_id
LEFT JOIN hr.regions r
    ON c.region_id = r.region_id
WHERE d.department_name IS NOT NULL
ORDER BY r.region_name, c.country_name, l.city;
"""

