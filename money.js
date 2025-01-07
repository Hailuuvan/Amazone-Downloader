function highlightTodayRow() {
  var sheet = SpreadsheetApp.getActiveSpreadsheet().getActiveSheet();
  var today = new Date(); // Lấy ngày hôm nay
  var todayDate = today.getDate(); // Lấy ngày hôm nay (chỉ ngày)
  
  // Lấy tất cả các ô trong hàng 3 từ C3 trở đi
  var range = sheet.getRange(3, 3, 1, sheet.getLastColumn() - 2); // Bắt đầu từ ô C3 (hàng 3, cột 3)
  var values = range.getValues(); // Lấy giá trị của tất cả các ô trong hàng 3

  // Duyệt qua các ô và kiểm tra nếu ngày trong ô trùng với ngày hôm nay
  for (var i = 0; i < values[0].length; i++) {
    var cellValue = values[0][i]; // Giá trị trong ô (là số ngày)
    
    // Kiểm tra nếu giá trị trong ô trùng với ngày hôm nay
    if (cellValue === todayDate) {
      // Tô màu nền ô nếu ngày trong ô trùng với ngày hôm nay
      console.log("Đã tô vàng"); // Tô màu vàng (hoặc bạn có thể thay đổi màu này)
    } else {
      // Xóa màu nền nếu không trùng
      console.log("trung mau")
    }
  }
}