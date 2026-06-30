from pydantic import BaseModel

class LoanInput(BaseModel):
    Age: int
    Income: int
    LoanAmount: int
    CreditScore: int
    MonthsEmployed: int
    NumCreditLines: int
    InterestRate: float
    LoanTerm: int
    DTIRatio: float

    Education: str
    EmploymentType: str
    MaritalStatus: str
    LoanPurpose: str

    HasMortgage: str
    HasDependents: str
    HasCoSigner: str
