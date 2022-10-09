# Import Module
from email import header
import tabula

tabula.convert_into("1.pdf", "1.txt",output_format="csv", pages='all',area=[140,12.75,790.5,950])