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
# Formata valores numéricos com duas casas decimais no pandas.
pd.set_option("display.float_format", "{:,.2f}".format)


def format_currency(value):
    return f"R$ {value:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")

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
print(f"Média: {format_currency(df1['SALARY'].mean())}")
print(f"Mediana: {format_currency(df1['SALARY'].median())}")
print(f"Mínimo: {format_currency(df1['SALARY'].min())}")
print(f"Máximo: {format_currency(df1['SALARY'].max())}")

# %% Cell 11
plt.figure(figsize=(8,5))
mean_salary = df1["SALARY"].mean()
median_salary = df1["SALARY"].median()
ax = plt.gca()
ax.hist(df1["SALARY"], bins=12, edgecolor="white", color="#4C78A8", alpha=0.9)
ax.axvline(mean_salary, color="#E45756", linestyle="--", linewidth=2, label=f"Média: {format_currency(mean_salary)}")
ax.axvline(median_salary, color="#54A24B", linestyle="-.", linewidth=2, label=f"Mediana: {format_currency(median_salary)}")
ax.set_title("Distribuição dos salários")
ax.set_xlabel("Salário")
ax.set_ylabel("Quantidade de funcionários")
ax.legend()
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
media_cargo_plot = media_cargo.sort_values()
fig, ax = plt.subplots(figsize=(9,5))
media_cargo_plot.plot(kind="barh", ax=ax, color="#F58518")
ax.set_title("Top 10 Cargos com Maior Média Salarial")
ax.set_xlabel("Salário Médio")
ax.set_ylabel("Cargo")
ax.bar_label(ax.containers[0], labels=[format_currency(v) for v in media_cargo_plot], padding=3, fontsize=8)
plt.tight_layout()
plt.savefig(OUTPUT_DIR / "top_10_cargos_maior_media_salarial.png", dpi=150, bbox_inches="tight")
if not RUNNING_AS_SCRIPT:
    plt.show()
plt.close()

# %% Cell 15
plt.figure(figsize=(12,6))
df1.boxplot(
    column="SALARY",
    by="DEPARTMENT_NAME",
    rot=90,
    grid=False,
    showmeans=True,
    meanprops={
        "marker": "o",
        "markerfacecolor": "#F58518",
        "markeredgecolor": "black",
        "markersize": 5,
    },
)
plt.title("Salário por Departamento")
plt.suptitle("")
plt.xlabel("Departamento")
plt.ylabel("Salário")
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
fig, ax = plt.subplots(figsize=(10,8))
cargo.plot(kind="barh", ax=ax, color="#54A24B")
ax.set_title("Média Salarial por Cargo")
ax.set_xlabel("Salário Médio")
ax.set_ylabel("Cargo")
ax.bar_label(ax.containers[0], labels=[format_currency(v) for v in cargo], padding=3, fontsize=8)
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

df_regiao = df.dropna(subset=["REGION_NAME"]).copy()

# %% Cell 19
df.shape

# %% Cell 20
df1.shape, df2.shape, df.shape, df_regiao.shape

# %% Cell 21
df_regiao.groupby("REGION_NAME")["SALARY"].mean().sort_values()

# %% Cell 22
media_regiao = df_regiao.groupby("REGION_NAME")["SALARY"].mean().sort_values()
fig, ax = plt.subplots(figsize=(7,4))
media_regiao.plot(kind="bar", ax=ax, color="#E45756")
ax.set_title("Média Salarial por Região")
ax.set_xlabel("Região")
ax.set_ylabel("Salário Médio")
ax.bar_label(ax.containers[0], labels=[format_currency(v) for v in media_regiao], padding=3)
plt.tight_layout()
plt.savefig(OUTPUT_DIR / "media_salarial_por_regiao.png", dpi=150, bbox_inches="tight")
if not RUNNING_AS_SCRIPT:
    plt.show()
plt.close()

# %% Cell 23
func_por_regiao = df_regiao["REGION_NAME"].value_counts().sort_values()
fig, ax = plt.subplots(figsize=(7,4))
func_por_regiao.plot(kind="barh", ax=ax, color="#4C78A8")
ax.set_title("Quantidade de Funcionários por Região")
ax.set_xlabel("Quantidade de Funcionários")
ax.set_ylabel("Região")
ax.bar_label(ax.containers[0], labels=[str(int(v)) for v in func_por_regiao], padding=3)
plt.tight_layout()
plt.savefig(OUTPUT_DIR / "quantidade_funcionarios_por_regiao.png", dpi=150, bbox_inches="tight")
if not RUNNING_AS_SCRIPT:
    plt.show()
plt.close()

# %% Cell 24
func_por_depto = df1["DEPARTMENT_NAME"].value_counts()
func_por_depto

# %% Cell 25
func_por_depto.sort_values().plot(kind="barh", figsize=(8,5), color="#72B7B2")
plt.title("Quantidade de Funcionarios por Departamento")
plt.xlabel("Quantidade de Funcionarios")
plt.ylabel("Departamento")
plt.tight_layout()
plt.savefig(OUTPUT_DIR / "quantidade_funcionarios_por_departamento.png", dpi=150, bbox_inches="tight")
if not RUNNING_AS_SCRIPT:
    plt.show()
plt.close()

# %% Cell 26
resumo_departamento = df1.groupby("DEPARTMENT_NAME").agg(
    MEDIA_SALARIAL=("SALARY", "mean"),
    QTD_FUNCIONARIOS=("EMPLOYEE_ID", "count")
).sort_values("MEDIA_SALARIAL", ascending=False)
resumo_departamento

# %% Cell 27
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

# %% Cell 28
Q1 = df1["SALARY"].quantile(0.25)
Q3 = df1["SALARY"].quantile(0.75)
IQR = Q3 - Q1
outliers = df1[
    (df1["SALARY"] < Q1 - 1.5 * IQR) |
    (df1["SALARY"] > Q3 + 1.5 * IQR)
]
outliers

# %% Cell 29
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

# %% Cell 30
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
