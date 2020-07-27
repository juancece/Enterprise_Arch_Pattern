from sqlalchemy import Table, MetaData, Column, Integer, String, Date
from sqlalchemy.orm import mapper, relationship

import model


metadata = MetaData()

order_lines = Table(
    'order_lines', metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('sku', String(255)),
    Column('qty', Integer, nullable=False),
    Column('orderid', String(255)),
)

batches = Table(
    'batches', metadata,
    Column('reference', String(255), primary_key=True),
    Column('sku', String(255), primary_key=True),
    Column('_purchase_qty', Integer),
    Column('eta', Date),
)


def start_mappers():
    lines_mapper = mapper(model.OrderLine, order_lines)
    mapper(model.Batch, batches)