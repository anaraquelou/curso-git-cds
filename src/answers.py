import pandas as pd
import plotly.express as px
import streamlit as st


def create_dataframe_section(df):
    st.title("Database Section")

    col_1, col_2 = st.columns(2)

    col_1.header("Database")
    col_1.dataframe(df, height=530)

    col_2.header("Data Description")

    data_description = """
                        | Coluna | Descrição |
                        | :----- | --------: |
                        | ID | Identificador da linha/registro |
                        | name | Fabricante e Modelo da Moto |
                        | selling_price | Preço de Venda |
                        | year | Ano de Fabricação da Moto |
                        | seller_type | Tipo de Vendedor - Se é vendedor pessoal ou revendedor |
                        | owner | Se é primeiro, segundo, terceiro ou quarto dono da moto |
                        | km_driven | Quantidade de Quilometros percorrido pela moto |
                        | ex_showroom_price | Preço da motocicleta sem as taxas de seguro e registro |
                        | age | Quantidade de anos em que a moto está em uso |
                        | km_class | Classificação das motos conforme a quilometragem percorrida |
                        | km_per_year | Quantidade de Quilometros percorridos a cada ano |
                        | km_per_month | Quantidade de Quilometros percorridos por mês |
                        | company | Fabricanete da Motocicleta |
    """

    col_2.markdown(data_description)

    return None


def rd1_question_9(df):
    df_grouped = df[["id", "seller_type"]].groupby("seller_type")

    df_grouped = df_grouped.count().reset_index()

    df_grouped = df_grouped.rename(columns={"id": "count"})

    fig = px.bar(
        df_grouped,
        x="seller_type",
        y="count",
        labels={"seller_type": "Seller Type", "count": "Quantity"},
        color="seller_type",
        text="count",
    )

    fig.update_traces(textposition="outside")

    st.plotly_chart(fig, use_container_width=True)

    return None


def rd1_question_13(df):
    df_grouped = (
        df.groupby("owner")
        .agg(qty=pd.NamedAgg("id", "count"))
        .sort_values("qty")
        .reset_index()
    )

    fig = px.bar(
        df_grouped,
        x="owner",
        y="qty",
        labels={"owner": "Owner Types", "qty": "Quantity"},
        color="owner",
        text="qty",
    )

    fig.update_traces(textposition="outside")

    st.plotly_chart(fig, use_container_width=True)

    return None


def rd1_question_14(df):
    st.text("As we can see, bikes with high kilometer have cheapier prices")

    fig = px.scatter(
        df,
        x="km_driven",
        y="selling_price",
        labels={"km_driven": "Kilometers", "selling_price": "Selling Price"},
    )

    st.plotly_chart(fig, use_container_width=True)

    return None