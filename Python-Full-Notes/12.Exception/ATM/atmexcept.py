#atmexcept.py
class DepositError(BaseException):pass

class WithdrawError(Exception):pass
class InSuffFundError(Exception):pass