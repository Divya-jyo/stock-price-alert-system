from sqlalchemy import create_engine, Column, Float, String, Integer, DateTime, Boolean
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime

DATABASE_URL = "postgresql+psycopg2://postgres:Divya2222@stock-alerts-db.cdksecuqgv47.us-east-2.rds.amazonaws.com/stock_alerts?sslmode=require"

engine = create_engine(DATABASE_URL)
Base = declarative_base()

# ✅ Your existing table (no change)
class StockPrice(Base):
    __tablename__ = "stock_prices"
    id = Column(Integer, primary_key=True)
    symbol = Column(String(10))
    price = Column(Float)
    change = Column(String(20))
    timestamp = Column(DateTime, default=datetime.now)

# 🆕 New table — stores alert rules
class Alert(Base):
    __tablename__ = "alerts"
    id = Column(Integer, primary_key=True)
    user_email = Column(String(120))
    stock_symbol = Column(String(10))
    threshold_price = Column(Float)
    condition = Column(String(10))   # "above" or "below"
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.now)

Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)

# ✅ Your existing function (no change)
def save_price(symbol, price, change):
    session = Session()
    record = StockPrice(symbol=symbol, price=price, change=change)
    session.add(record)
    session.commit()
    session.close()
    print(f"✅ Saved {symbol} price ${price} to database!")

# 🆕 Save a new alert
def save_alert(email, symbol, threshold_price, condition):
    session = Session()
    alert = Alert(
        user_email=email,
        stock_symbol=symbol,
        threshold_price=threshold_price,
        condition=condition
    )
    session.add(alert)
    session.commit()
    session.close()
    print(f"✅ Alert saved for {symbol}!")

# 🆕 Get all active alerts
def get_active_alerts():
    session = Session()
    alerts = session.query(Alert).filter_by(is_active=True).all()
    session.close()
    return alerts

# 🆕 Disable alert after it triggers
def disable_alert(alert_id):
    session = Session()
    alert = session.query(Alert).filter_by(id=alert_id).first()
    if alert:
        alert.is_active = False
        session.commit()
    session.close()

print("✅ Database connected and tables created!")