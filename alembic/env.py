from logging.config import fileConfig
from sqlalchemy import engine_from_config, pool
from alembic import context
from journal_app.models import Base 
from journal_app.database import engine  

target_metadata = Base.metadata

if context.config.config_file_name:
    fileConfig(context.config.config_file_name)

context.configure(
    url=engine.url if engine else None,
    target_metadata=target_metadata,
    render_as_batch=True,
    dialect_opts={},
)

def run_migrations_offline():
    context.configure(
        url='sqlite:///./grade_journal.db',
        target_metadata=target_metadata,
        literal_binds=False,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online():
    if engine is None:
        raise Exception("Engine is None")

    connectable = engine_from_config(
        context.config.get_section(context.config.config_ini_section),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
        )

        with context.begin_transaction():
            context.run_migrations()

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
