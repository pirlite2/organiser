#******************************************************************************
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA. 
#******************************************************************************

def iso8601_to_tuple(deadline):
	""" Convert ISO8601 format to date/time tuple """

	year = (deadline - (deadline % 100000000)) // 100000000
	deadline -= year * 100000000
	month = (deadline - (deadline % 1000000)) // 1000000
	deadline -= month * 1000000
	days = (deadline - (deadline % 10000)) // 10000
	deadline -= days * 10000
	hours = (deadline - (deadline % 100)) // 100
	minutes = deadline - (hours * 100)

	return (hours, minutes, days, month, year)

#--------------------------------------------------------------------------

def tuple_to_iso8601(deadline_tuple):
	""" Convert date/time tuple to ISO8601 format """

	(hours, minutes, days, month, year) = deadline_tuple
	deadline = year * 100000000
	deadline += month * 1000000
	deadline += days * 10000
	deadline += hours * 100
	deadline += minutes

	return deadline

#******************************************************************************

if __name__ == "__main__":

	# Test code
	dateTime = (14, 32, 17, 6, 2020)
	iso8601_dateTime = tuple_to_iso8601(dateTime)
	print(iso8601_dateTime)
	print(iso8601_to_tuple(iso8601_dateTime))

#******************************************************************************