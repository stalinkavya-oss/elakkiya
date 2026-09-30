from sqlalchemy.orm import Session

from ..database import Expense


def create_expense(
    db: Session,
    user_id: int,
    title: str,
    amount: float,
    category: str,
    description: str | None = None
):
    expense = Expense(
        user_id=user_id,
        title=title,
        amount=amount,
        category=category,
        description=description
    )

    db.add(expense)
    db.commit()
    db.refresh(expense)

    return expense


def get_user_expenses(
    db: Session,
    user_id: int
):
    return (
        db.query(Expense)
        .filter(Expense.user_id == user_id)
        .order_by(Expense.id.desc())
        .all()
    )


def delete_expense(
    db: Session,
    user_id: int,
    expense_id: int
):
    expense = (
        db.query(Expense)
        .filter(
            Expense.id == expense_id,
            Expense.user_id == user_id
        )
        .first()
    )

    if not expense:
        return False

    db.delete(expense)
    db.commit()

    return True