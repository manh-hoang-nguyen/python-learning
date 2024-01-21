from flat import Bill, Flatmate
from reports import PdfReport

bill = Bill(30, "July 2023")
hoang = Flatmate(name="Hoang", days_in_house=15)
maxime = Flatmate(name="maxime", days_in_house=10)
hoang_to_pay = hoang.pays(bill=bill, flatmate2=maxime)
print(hoang_to_pay)

pdf_report = PdfReport(filename=f"{bill.period}.pdf")
pdf_report.generate(hoang, maxime, bill)
