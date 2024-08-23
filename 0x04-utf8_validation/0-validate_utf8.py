#!/usr/bin/python3

def count_consecutive_ones(byte):
  """
  This function counts the number of consecutive leading 1's in the binary representation of a byte.
  """
  count = 0
  while byte & 0x80 != 0:
    count += 1
    byte <<= 1
  return count

def validUTF8(data):
  """
  This function determines if a given list of integers represents a valid UTF-8 encoding.

  Args:
    data: A list of integers representing bytes.

  Returns:
    True if the data is a valid UTF-8 encoding, False otherwise.
  """

  # Track the number of continuation bytes expected for a multi-byte character.
  continuation_bytes = 0
  for byte in data:
    # Extract the 8 least significant bits.
    byte = byte & 0xFF

    # Check for single-byte characters (0xxxxxxx)
    if continuation_bytes == 0:
      if byte < 0x80:
        continue
      # Check for invalid starting byte patterns for multi-byte characters.
      elif byte & 0xC0 == 0xC0:
        continuation_bytes = 1  # Expecting one continuation byte.
      elif byte & 0xE0 == 0xE0:
        continuation_bytes = 2  # Expecting two continuation bytes.
      elif byte & 0xF0 == 0xF0:
        continuation_bytes = 3  # Expecting three continuation bytes.
      else:
        return False  # Invalid starting byte pattern for multi-byte character.
    # Check for continuation bytes (10xxxxxx)
    else:
      if byte & 0xC0 != 0x80:
        return False  # Invalid continuation byte pattern.
      continuation_bytes -= 1

  # Check if any continuation bytes are still expected at the end.
  return continuation_bytes == 0

# Make the script executable
if __name__ == "__main__":
  pass
