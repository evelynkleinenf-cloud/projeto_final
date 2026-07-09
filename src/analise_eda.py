# Auto-generated from notebooks/Notebook_Evelyn.ipynb

# %% Cell 0
from pathlib import Path

try:
    PROJECT_DIR = Path(__file__).resolve().parent.parent
except NameError:
    BASE_DIR = Path.cwd()
    if (BASE_DIR / "data").exists():
        PROJECT_DIR = BASE_DIR
    elif (BASE_DIR.parent / "data").exists():
        PROJECT_DIR = BASE_DIR.parent
    else:
        PROJECT_DIR = BASE_DIR

DATA_DIR = PROJECT_DIR / "data"
OUTPUT_DIR = PROJECT_DIR / "outputs" / "figures"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

import matplotlib
RUNNING_AS_SCRIPT = "__file__" in globals()
if RUNNING_AS_SCRIPT:
    matplotlib.use("Agg")

import pandas as pd
import matplotlib.pyplot as plt

plt.style.use("seaborn-v0_8-whitegrid")
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
print(f"Media: {df1['SALARY'].mean():.2f}")
print(f"Mediana: {df1['SALARY'].median():.2f}")
print(f"Minimo: {df1['SALARY'].min():.2f}")
print(f"Maximo: {df1['SALARY'].max():.2f}")

# %% Cell 11
plt.figure(figsize=(8,5))
plt.hist(df1["SALARY"], bins=10, edgecolor="black", color="#4C78A8")
plt.title("Distribuicao dos salarios")
plt.xlabel("Salario")
plt.ylabel("Quantidade de funcionarios")
plt.tight_layout()
plt.savefig(OUTPUT_DIR / "histograma_salarios.png", dpi=150, bbox_inches="tight")
if not RUNNING_AS_SCRIPT:
    plt.show()
plt.close()

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
media_cargo.sort_values().plot(kind="barh", figsize=(9,5), color="#F58518")
plt.title("Top 10 Cargos com Maior Media Salarial")
plt.xlabel("Salario Medio")
plt.ylabel("Cargo")
plt.tight_layout()
plt.savefig(OUTPUT_DIR / "top_10_cargos_maior_media_salarial.png", dpi=150, bbox_inches="tight")
if not RUNNING_AS_SCRIPT:
    plt.show()
plt.close()

# %% Cell 15
plt.figure(figsize=(12,6))
df1.boxplot(column="SALARY", by="DEPARTMENT_NAME", rot=90)
plt.title("Salario por Departamento")
plt.suptitle("")
plt.xlabel("Departamento")
plt.ylabel("Salario")
plt.tight_layout()
plt.savefig(OUTPUT_DIR / "boxplot_salario_por_departamento.png", dpi=150, bbox_inches="tight")
if not RUNNING_AS_SCRIPT:
    plt.show()
plt.close()

# %% Cell 16
cargo = (
    df1.groupby("JOB_TITLE")["SALARY"]
    .mean()
    .sort_values()
)
plt.figure(figsize=(10,8))
cargo.plot(kind="barh", color="#54A24B")
plt.title("Media Salarial por Cargo")
plt.xlabel("Salario Medio")
plt.ylabel("Cargo")
plt.tight_layout()
plt.savefig(OUTPUT_DIR / "media_salarial_por_cargo.png", dpi=150, bbox_inches="tight")
if not RUNNING_AS_SCRIPT:
    plt.show()
plt.close()

# %% Cell 17
print("Query 1:", df1.shape)
print("Query 2:", df2.shape)

# %% Cell 18
df = pd.merge(
    df1,
    df2[["EMPLOYEE_ID", "REGION_NAME"]],
    on="EMPLOYEE_ID",
    how="left"
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
    figsize=(7,4),
    color="#E45756"
)
plt.title("Media Salarial por Regiao")
plt.xlabel("Regiao")
plt.ylabel("Salario Medio")
plt.tight_layout()
plt.savefig(OUTPUT_DIR / "media_salarial_por_regiao.png", dpi=150, bbox_inches="tight")
if not RUNNING_AS_SCRIPT:
    plt.show()
plt.close()

# %% Cell 23
func_por_depto = df1["DEPARTMENT_NAME"].value_counts()
func_por_depto

# %% Cell 24
func_por_depto.sort_values().plot(kind="barh", figsize=(8,5), color="#72B7B2")
plt.title("Quantidade de Funcionarios por Departamento")
plt.xlabel("Quantidade de Funcionarios")
plt.ylabel("Departamento")
plt.tight_layout()
plt.savefig(OUTPUT_DIR / "quantidade_funcionarios_por_departamento.png", dpi=150, bbox_inches="tight")
if not RUNNING_AS_SCRIPT:
    plt.show()
plt.close()

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
        "Ate R$4.000",
        "R$4.001-7.000",
        "R$7.001-10.000",
        "Acima de R$10.000"
    ]
)
faixas.value_counts().sort_index().plot(
    kind="bar",
    figsize=(8,4),
    color="#B279A2"
)
plt.title("Distribuicao dos Funcionarios por Faixa Salarial")
plt.xlabel("Faixa Salarial")
plt.ylabel("Quantidade")
plt.tight_layout()
plt.savefig(OUTPUT_DIR / "distribuicao_por_faixa_salarial.png", dpi=150, bbox_inches="tight")
if not RUNNING_AS_SCRIPT:
    plt.show()
plt.close()

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

