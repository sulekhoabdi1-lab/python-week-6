# Week 6 Assignment: Safe Functions

## Files

- safe_tools.py - Contains three safe functions that handle division errors, invalid numbers, and missing dictionary keys.
- README.md - Describes the assignment files and explains why an if check alone cannot catch invalid number input.

## Why can the if check not catch "abc" on its own?

An if check can check conditions before converting text into a number, but it cannot catch a ValueError raised by int("abc"). The try/except block catches this specific error and prevents the program from crashing.