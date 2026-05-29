**Pytest uchun test kod**
```python
import pytest
import csv
from csv_writer import CSVWriter

@pytest.fixture
def csv_writer():
    return CSVWriter()

def test_csv_writer_write_row(csv_writer):
    csv_writer.write_row(["Name", "Age", "City"])
    with open("test.csv", "r") as file:
        reader = csv.reader(file)
        rows = list(reader)
        assert rows == [["Name", "Age", "City"]]

def test_csv_writer_write_data(csv_writer):
    csv_writer.write_row(["John", 25, "New York"])
    csv_writer.write_row(["Alice", 30, "Los Angeles"])
    with open("test.csv", "r") as file:
        reader = csv.reader(file)
        rows = list(reader)
        assert rows == [["Name", "Age", "City"], ["John", "25", "New York"], ["Alice", "30", "Los Angeles"]]

def test_csv_writer_close_file(csv_writer):
    csv_writer.write_row(["Name", "Age", "City"])
    csv_writer.close()
    assert csv_writer.file.closed == True
```

**Jest uchun test kod**
```javascript
const fs = require('fs');
const csvWriter = require('./csv_writer');

describe('CSVWriter', () => {
  let csvWriter;

  beforeEach(() => {
    csvWriter = new csvWriter.CSVWriter();
  });

  afterEach(() => {
    fs.unlinkSync('test.csv');
  });

  it('should write row to csv file', () => {
    csvWriter.writeRow(["Name", "Age", "City"]);
    const data = fs.readFileSync('test.csv', 'utf8');
    const rows = data.split('\n');
    expect(rows).toEqual(["Name,Age,City"]);
  });

  it('should write data to csv file', () => {
    csvWriter.writeRow(["Name", "Age", "City"]);
    csvWriter.writeRow(["John", 25, "New York"]);
    csvWriter.writeRow(["Alice", 30, "Los Angeles"]);
    const data = fs.readFileSync('test.csv', 'utf8');
    const rows = data.split('\n');
    expect(rows).toEqual(["Name,Age,City","John,25,New York","Alice,30,Los Angeles"]);
  });

  it('should close file after writing', () => {
    csvWriter.writeRow(["Name", "Age", "City"]);
    csvWriter.close();
    expect(csvWriter.file.closed).toBe(true);
  });
});
```
