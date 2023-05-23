using MySqlConnector;
using System;
using System.Collections.Generic;
using System.Data;
using System.Linq;
using System.Security.Principal;
using System.Text;
using System.IO;
using System.Threading.Tasks;
using System.Data.SqlTypes;
using System.Security.Cryptography.X509Certificates;

namespace ace_access_system
{

    public class Address_book
    {
        internal void ExportToCsv(DataTable dataTable)
        {
            // 設定文件儲存對話框
            SaveFileDialog saveFileDialog = new SaveFileDialog();
            saveFileDialog.Filter = "CSV 文件 (*.csv)|*.csv";
            saveFileDialog.FileName = "Export.csv";
            saveFileDialog.Title = "導出到 CSV 文件";
            saveFileDialog.ShowDialog();

            // 如果使用者選擇了文件儲存路徑
            if (saveFileDialog.FileName != "")
            {
                StringBuilder stringBuilder = new StringBuilder(); // 建立 StringBuilder(要修改字串而不建立新的物件)
                // 添加欄位標題
                foreach (DataColumn column in dataTable.Columns)
                {
                    stringBuilder.Append(column.ColumnName + ",");
                }
                try 
                {
                    if (stringBuilder.Length > 0)
                    {
                        stringBuilder.Remove(stringBuilder.Length - 1, 1); //刪除最後字符
                    }
                }
                catch (Exception e)
                {
                    Console.WriteLine(e.Message);
                }
                             
                stringBuilder.Append(Environment.NewLine);

                // 添加每一列的資料
                foreach (DataRow row in dataTable.Rows)
                {                    
                    foreach (DataColumn column in dataTable.Columns)
                    {
                        stringBuilder.Append(row[column].ToString().Replace(",", " ") + ",");
                    }
                    stringBuilder.Remove(stringBuilder.Length - 1, 1); 
                    stringBuilder.Append(Environment.NewLine);
                }

                // 寫入CSV檔案
                using (StreamWriter sw = new StreamWriter(saveFileDialog.FileName, false, Encoding.UTF8))
                {
                    sw.Write(stringBuilder.ToString());
                }

                MessageBox.Show("導出成功！", "提示", MessageBoxButtons.OK, MessageBoxIcon.Information);
            }
            else
            {
                MessageBox.Show("請選擇文件儲存路徑！", "提示", MessageBoxButtons.OK, MessageBoxIcon.Information);

            }
        } //導出

    }
}
