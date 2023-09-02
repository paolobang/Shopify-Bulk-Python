from lineitems import line_items

orders="""
    orders{{
        edges {{
            node {{
                id
                createdAt
                currentSubtotalLineItemsQuantity
                {lineItems}
            }}
        }}
    }}
""".format(lineItems=line_items)