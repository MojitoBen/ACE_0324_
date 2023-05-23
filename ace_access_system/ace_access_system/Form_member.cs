using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.Data;
using static System.Windows.Forms.VisualStyles.VisualStyleElement;
using static System.Windows.Forms.VisualStyles.VisualStyleElement.ToolBar;
using static System.Windows.Forms.VisualStyles.VisualStyleElement.Button;
using System.Security.Principal;
using System.Reflection;
using System.Xml;
using MySqlConnector;
using System.IO;
using static ace_access_system.Address_book;
using static ace_access_system.Static_Class;
using System.Drawing.Imaging;
using System.ComponentModel.DataAnnotations;
using System.Diagnostics;
using MySqlX.XDevAPI.Relational;

namespace ace_access_system
{
    public partial class Form_member : Form
    {
        private Address_book address_book = new Address_book();
        //[變數]判斷目前radio事件所選值
        private string identity = "";
        //[布林]判斷按下確定或取消
        private bool shouldPerformOperation = false;
        //判斷目前欄位是按下新建、修改、刪除
        private string currentOperation = "";
        //照片ID
        public string? PhotoId;
        public Form_member()
        {
            InitializeComponent();
            //判斷是否僅輸入數字
            textBox_num.KeyPress += TextBoxHelper.Str_Keypress;
            textBox_cardnum.KeyPress += TextBoxHelper.Str_Keypress;
            textBox_postcode.KeyPress += TextBoxHelper.Str_Keypress;
            textBox_phone.KeyPress += TextBoxHelper.Str_Keypress;
            textBox_numC.KeyPress += TextBoxHelper.Str_Keypress;
            textBox_cardnumC.KeyPress += TextBoxHelper.Str_Keypress;
            KeyPreview = true;
        }

        private void Form_member_Load(object sender, EventArgs e)
        {
            Renew();
        }


        private void Renew()
        {
            button_add.Enabled = true;
            button_revise.Enabled = true;
            button_del.Enabled = true;
            button_export.Enabled = true;
            panel_info.Enabled = false;
            panel_info.BackColor = Color.LightBlue;
            pictureBox_photo.Image = null;
            panel5.Enabled = false;
            SQL_Conn.cn.Close();
            try
            {
                string sql = "SELECT * From `asc_access`.`name_list`";
                MySqlCommand cmd = new MySqlCommand(sql, SQL_Conn.cn);
                SQL_Conn.cn.Open();
                MySqlDataReader reader = cmd.ExecuteReader();
                dataGridView_SQL.Rows.Clear();
                while (reader.Read())
                {
                    int index = this.dataGridView_SQL.Rows.Add();

                    this.dataGridView_SQL.Rows[index].Cells[0].Value = reader.GetString("Num");
                    this.dataGridView_SQL.Rows[index].Cells[1].Value = reader.GetString("Name");
                    this.dataGridView_SQL.Rows[index].Cells[2].Value = reader.GetString("CardNum");
                    this.dataGridView_SQL.Rows[index].Cells[3].Value = reader.GetString("Identity");
                    this.dataGridView_SQL.Rows[index].Cells[4].Value = reader.GetDateTime("Birth");
                    this.dataGridView_SQL.Rows[index].Cells[5].Value = reader.GetString("IDNum");
                    this.dataGridView_SQL.Rows[index].Cells[6].Value = reader.GetString("Postcode");
                    this.dataGridView_SQL.Rows[index].Cells[7].Value = reader.GetString("Address");
                    this.dataGridView_SQL.Rows[index].Cells[8].Value = reader.GetString("Phone");
                    this.dataGridView_SQL.Rows[index].Cells[9].Value = reader.GetString("HPhone");
                    this.dataGridView_SQL.Rows[index].Cells[10].Value = reader.GetDateTime("Entrant");
                    this.dataGridView_SQL.Rows[index].Cells[11].Value = reader.GetDateTime("Resign");
                    this.dataGridView_SQL.Rows[index].Cells[12].Value = reader.GetString("Depart");
                    this.dataGridView_SQL.Rows[index].Cells[13].Value = reader.GetString("Marry");
                    this.dataGridView_SQL.Rows[index].Cells[14].Value = reader.GetString("Gender");
                    this.dataGridView_SQL.Rows[index].Cells[15].Value = reader.GetString("Note");
                }
                reader.Close();
                cmd.ExecuteNonQuery();
                SQL_Conn.cn.Close();
            }
            catch (MySql.Data.MySqlClient.MySqlException ex)
            {
                LogRecord.WriteLog(ex.Message, "form_member");
            }
        } //更新介面


        private void button_add_Click(object sender, EventArgs e)
        {
            currentOperation = "Add";
            button_revise.Enabled = false;
            button_del.Enabled = false;
            button_export.Enabled = true;
            panel_info.Enabled = true;
            Clear_panel_info();
            radioButton_user.Checked = true;
            pictureBox_photo.Image = null;
            panel5.Enabled = false;
        } //點擊新增按鈕事件
        private void button_revise_Click(object sender, EventArgs e)
        {
            currentOperation = "Revise";
            button_add.Enabled = false;
            button_del.Enabled = false;
            button_export.Enabled = true;
            panel_info.Enabled = true;
            pictureBox_photo.Image = null;
            panel5.Enabled = false;
            Clear_panel_info();
            Fill_panel_info();
        } //點擊修改按鈕事件
        private void button_del_Click(object sender, EventArgs e)
        {
            currentOperation = "Delete";
            button_add.Enabled = false;
            button_revise.Enabled = false;
            button_export.Enabled = false;
            panel_info.Enabled = true;
            panel5.Enabled = false;
            Clear_panel_info();
            Fill_panel_info();
            panel_info.BackColor = Color.Red;
        } //點擊刪除按鈕事件
        private void button_close_Click(object sender, EventArgs e)
        {
            this.Close();
        } //離開當前視窗
        private void button_enter_Click(object sender, EventArgs e)
        {
            string Enable_status;
            if (checkBox_door_permission.Checked == true)
            {
                Enable_status = "1";
            }
            else 
            {
                Enable_status = "0";
            }
            if (identity is null)
            {
                identity = "使用者";
            }

            if (currentOperation == "Add")
            {
                DialogResult add_result = MessageBox.Show("您確定要新增嗎?", "確定新增", MessageBoxButtons.YesNo, MessageBoxIcon.Question);
                if (add_result == DialogResult.Yes)
                {
                    shouldPerformOperation = true;
                    //會員資料
                    MySqlCommand cmd = new MySqlCommand();
                    string str = "INSERT INTO name_list (Num, Name, CardNum, Identity, Birth, IDNum, Postcode, Address, Phone, HPhone, Entrant, Resign, Depart, Marry, Gender, Note) " +
                                    "VALUES (@Num, @Name, @CardNum, @Identity, @Birth, @IDNum, @Postcode, @Address, @Phone, @HPhone, @Entrant, @Resign, @Depart, @Marry, @Gender, @Note)";

                    cmd.Parameters.AddWithValue("@Num", textBox_num.Text);
                    cmd.Parameters.AddWithValue("@Name", textBox_name.Text);
                    cmd.Parameters.AddWithValue("@CardNum", textBox_cardnum.Text);
                    cmd.Parameters.AddWithValue("@Identity", identity);
                    cmd.Parameters.AddWithValue("@Birth", dateTimePicker_birth.Value);
                    cmd.Parameters.AddWithValue("@IDNum", textBox_idnum.Text);
                    cmd.Parameters.AddWithValue("@Postcode", textBox_postcode.Text);
                    cmd.Parameters.AddWithValue("@Address", textBox_address.Text);
                    cmd.Parameters.AddWithValue("@Phone", textBox_phone.Text);
                    cmd.Parameters.AddWithValue("@HPhone", textBox_hphone.Text);
                    cmd.Parameters.AddWithValue("@Entrant", dateTimePicker_entrant.Value);
                    cmd.Parameters.AddWithValue("@Resign", dateTimePicker_resign.Value);
                    cmd.Parameters.AddWithValue("@Depart", comboBox_depart.Text);
                    cmd.Parameters.AddWithValue("@Marry", comboBox_marry.Text);
                    cmd.Parameters.AddWithValue("@Gender", comboBox_gender.Text);
                    cmd.Parameters.AddWithValue("@Note", textBox_note.Text);
                    cmd.CommandText = str;
                    cmd.Connection = SQL_Conn.cn;
                    //門禁資料
                    MySqlCommand cmd2 = new MySqlCommand();
                    string door_p = "INSERT INTO door_permission (CardNum, Start_Date, End_Date, End_Time, Enable) " +
                                    "VALUES (@CardNum, @Start_Date, @End_Date, @End_Time, @Enable)";
                    cmd2.Parameters.AddWithValue("@CardNum", textBox_cardnum.Text);
                    cmd2.Parameters.AddWithValue("@Start_Date", dateTimePicker_start.Value);
                    cmd2.Parameters.AddWithValue("@End_Date", dateTimePicker_deadline.Value);
                    cmd2.Parameters.AddWithValue("@End_Time", dateTimePicker_deadlineT.Value);
                    cmd2.Parameters.AddWithValue("@Enable", Enable_status);
                    cmd2.CommandText = door_p;
                    cmd2.Connection = SQL_Conn.cn;

                    SQL_Conn.cn.Open();
                    if (panel5.Enabled == true)
                    {
                        Debug.WriteLine("Enable_status : " + Enable_status);
                        cmd2.ExecuteNonQuery();
                    }
                    MySqlCommand cmd_check_Num = new MySqlCommand("SELECT COUNT(*) FROM name_list WHERE Num = @Num", SQL_Conn.cn);
                    MySqlCommand cmd_check_CardNum = new MySqlCommand("SELECT COUNT(*) FROM name_list WHERE CardNum = @CardNum", SQL_Conn.cn);
                    cmd_check_Num.Parameters.AddWithValue("@Num", textBox_num.Text);
                    int count_check_Num = Convert.ToInt32(cmd_check_Num.ExecuteScalar());
                    cmd_check_CardNum.Parameters.AddWithValue("@CardNum", textBox_cardnum.Text);
                    int count_check_CardNum = Convert.ToInt32(cmd_check_CardNum.ExecuteScalar());
                    //一些輸入判定
                    if (string.IsNullOrEmpty(textBox_num.Text)) { MessageBox.Show("請輸入工號"); SQL_Conn.cn.Close(); return; }
                    else if (string.IsNullOrEmpty(textBox_cardnum.Text)) { MessageBox.Show("請輸入卡號"); SQL_Conn.cn.Close(); return; }
                    else if (string.IsNullOrEmpty(identity)) { MessageBox.Show("請點選身分"); SQL_Conn.cn.Close(); return; }
                    else if (count_check_Num > 0) { MessageBox.Show("工號已存在！"); SQL_Conn.cn.Close(); return; }
                    else if (count_check_CardNum > 0) { MessageBox.Show("卡號已存在！"); SQL_Conn.cn.Close(); return; }
                    else if (!string.IsNullOrEmpty(textBox_idnum.Text) && !System.Text.RegularExpressions.Regex.IsMatch(textBox_idnum.Text, @"^[A-Z]\d{9}$")) { MessageBox.Show("請確認身分證字號(大寫英文字母加九位數字)"); SQL_Conn.cn.Close(); return; }
                    else
                    {
                        int rowsAffected = cmd.ExecuteNonQuery();
                        if (rowsAffected > 0)
                        {
                            MessageBox.Show("新增成功");
                        }
                        else
                        {
                            MessageBox.Show("新增失敗");
                        }
                        Clear_panel_info();
                        SQL_Conn.cn.Close();
                        Renew();
                    }
                }
                else
                {
                    shouldPerformOperation = false;
                }

            } //"新增"的程式碼
            else if (currentOperation == "Revise")
            {
                DialogResult add_result = MessageBox.Show("您確定要修改嗎?", "確定修改", MessageBoxButtons.YesNo, MessageBoxIcon.Question);
                if (add_result == DialogResult.Yes)
                {
                    shouldPerformOperation = true;

                    if (dataGridView_SQL.SelectedRows.Count > 0)
                    {
                        // 獲取所選擇行的值
                        int selectedRowIndex = dataGridView_SQL.SelectedRows[0].Index;
                        int selectedID = Convert.ToInt32(dataGridView_SQL.Rows[selectedRowIndex].Cells[0].Value);
                        SQL_Conn.cn.Open();
                        MySqlCommand checkCmd = new MySqlCommand("SELECT COUNT(*) FROM `door_permission` WHERE `CardNum`=@CardNum", SQL_Conn.cn);
                        checkCmd.Parameters.AddWithValue("@CardNum", textBox_cardnum.Text);
                        int doorPermissionCount = Convert.ToInt32(checkCmd.ExecuteScalar());
                        
                        //門禁資料(修改)
                        if (doorPermissionCount > 0)
                        {
                            MySqlCommand cmd2 = new MySqlCommand("UPDATE `door_permission` SET `Start_Date`=@Start_Date, `End_Date`=@End_Date, `End_Time`=@End_Time, `Enable`=@Enable " +
                                                                  "WHERE `CardNum`=@CardNum", SQL_Conn.cn);
                            cmd2.Parameters.AddWithValue("@Start_Date", dateTimePicker_start.Value);
                            cmd2.Parameters.AddWithValue("@End_Date", dateTimePicker_deadline.Value);
                            cmd2.Parameters.AddWithValue("@End_Time", dateTimePicker_deadlineT.Value);
                            cmd2.Parameters.AddWithValue("@Enable", Enable_status);
                            cmd2.Parameters.AddWithValue("@CardNum", textBox_cardnum.Text);
                            int d_rowsAffected = cmd2.ExecuteNonQuery();

                            if (d_rowsAffected > 0)
                            {
                                MessageBox.Show("門禁修改成功");
                            }
                            else
                            {
                                MessageBox.Show("門禁修改失敗");
                            }
                        }
                        else
                        {
                            MySqlCommand cmd2 = new MySqlCommand("INSERT INTO `door_permission` (`CardNum`, `Start_Date`, `End_Date`, `End_Time`, `Enable`) " +
                                                                  "VALUES (@CardNum, @Start_Date, @End_Date, @End_Time, @Enable)", SQL_Conn.cn);
                            cmd2.Parameters.AddWithValue("@CardNum", textBox_cardnum.Text);
                            cmd2.Parameters.AddWithValue("@Start_Date", dateTimePicker_start.Value);
                            cmd2.Parameters.AddWithValue("@End_Date", dateTimePicker_deadline.Value);
                            cmd2.Parameters.AddWithValue("@End_Time", dateTimePicker_deadlineT.Value);
                            cmd2.Parameters.AddWithValue("@Enable", Enable_status);
                            int d_rowsAffected = cmd2.ExecuteNonQuery();

                            if (d_rowsAffected > 0)
                            {
                                MessageBox.Show("門禁新增成功");
                            }
                            else
                            {
                                MessageBox.Show("門禁新增失敗");
                            }
                        }


                        MySqlCommand cmd = new MySqlCommand("UPDATE `name_list` SET `Num`=@Num, `Name`=@Name, `CardNum`=@CardNum, `Identity`=@Identity, `Birth`=@Birth, `IDNum`=@IDNum, " +
                                                             "`Postcode`=@Postcode, `Address`=@Address, `Phone`=@Phone, `HPhone`=@HPhone, `Entrant`=@Entrant, `Resign`=@Resign, " +
                                                             "`Depart`=@Depart, `Marry`=@Marry, `Gender`=@Gender, `Note`=@Note WHERE `Num`=@Num", SQL_Conn.cn);                        
                        cmd.Parameters.AddWithValue("@Num", textBox_num.Text);
                        cmd.Parameters.AddWithValue("@Name", textBox_name.Text);
                        cmd.Parameters.AddWithValue("@CardNum", textBox_cardnum.Text);
                        cmd.Parameters.AddWithValue("@Identity", identity);
                        cmd.Parameters.AddWithValue("@Birth", dateTimePicker_birth.Value);
                        cmd.Parameters.AddWithValue("@IDNum", textBox_idnum.Text);
                        cmd.Parameters.AddWithValue("@Postcode", textBox_postcode.Text);
                        cmd.Parameters.AddWithValue("@Address", textBox_address.Text);
                        cmd.Parameters.AddWithValue("@Phone", textBox_phone.Text);
                        cmd.Parameters.AddWithValue("@HPhone", textBox_hphone.Text);
                        cmd.Parameters.AddWithValue("@Entrant", dateTimePicker_entrant.Value);
                        cmd.Parameters.AddWithValue("@Resign", dateTimePicker_resign.Value);
                        cmd.Parameters.AddWithValue("@Depart", comboBox_depart.Text);
                        cmd.Parameters.AddWithValue("@Marry", comboBox_marry.Text);
                        cmd.Parameters.AddWithValue("@Gender", comboBox_gender.Text);
                        cmd.Parameters.AddWithValue("@Note", textBox_note.Text);

                        if (string.IsNullOrEmpty(textBox_num.Text)) { MessageBox.Show("請輸入工號"); }
                        else if (string.IsNullOrEmpty(textBox_cardnum.Text)) { MessageBox.Show("請輸入卡號"); }
                        else if (string.IsNullOrEmpty(identity)) { MessageBox.Show("請點選身分"); }
                        else if (!string.IsNullOrEmpty(textBox_idnum.Text) && !System.Text.RegularExpressions.Regex.IsMatch(textBox_idnum.Text, @"^[A-Z]\d{9}$")) { MessageBox.Show("請確認身分證字號(大寫英文字母加九位數字)"); SQL_Conn.cn.Close(); return; }
                        int rowsAffected = cmd.ExecuteNonQuery();

                        if (rowsAffected > 0)
                        {
                            MessageBox.Show("修改成功");
                        }
                        else
                        {
                            MessageBox.Show("修改失敗");
                        }
                        SQL_Conn.cn.Close();
                        Renew();
                    }
                }
                else
                {
                    shouldPerformOperation = false;
                }
            } //"修改"的程式碼
            else if (currentOperation == "Delete")
            {
                DialogResult add_result = MessageBox.Show("您確定要刪除嗎?", "確定刪除", MessageBoxButtons.YesNo, MessageBoxIcon.Question);
                if (add_result == DialogResult.Yes)
                {
                    if (dataGridView_SQL.SelectedRows.Count > 0)
                    {
                        int selectedRowIndex = dataGridView_SQL.SelectedRows[0].Index;
                        int selectedID = Convert.ToInt32(dataGridView_SQL.Rows[selectedRowIndex].Cells[0].Value);
                        int selectedCardNum = Convert.ToInt32(dataGridView_SQL.Rows[selectedRowIndex].Cells[2].Value);

                        MySqlCommand cmd = new MySqlCommand("DELETE FROM `asc_access`.`name_list` WHERE Num = @Num", SQL_Conn.cn);
                        MySqlCommand del_cmd = new MySqlCommand("DELETE FROM `asc_access`.`photos` WHERE PhotoId = @photoid", SQL_Conn.cn);
                        MySqlCommand door_cmd = new MySqlCommand("DELETE FROM `asc_access`.`door_permission` WHERE CardNum = @CardNum", SQL_Conn.cn);
                        PhotoId = this.textBox_num.Text;
                        SQL_Conn.cn.Open();
                        cmd.Parameters.AddWithValue("@Num", selectedID);
                        del_cmd.Parameters.AddWithValue("@photoid", PhotoId);
                        door_cmd.Parameters.AddWithValue("@CardNum", selectedCardNum);
                        int del_rowsAffected = del_cmd.ExecuteNonQuery();
                        int door_rowsAffected = door_cmd.ExecuteNonQuery();
                        int rowsAffected = cmd.ExecuteNonQuery();

                        if (rowsAffected > 0 | door_rowsAffected >= 0 | del_rowsAffected >= 0)
                        {
                            MessageBox.Show("刪除成功！");
                            Renew();
                        }
                        else
                        {
                            MessageBox.Show("刪除失敗！");
                        }
                    }
                    else
                    {
                        MessageBox.Show("請先選擇要刪除的行！");
                    }
                }
                SQL_Conn.cn.Close();

            } //"刪除"的程式碼
        } //新增修改刪除的確定選項加上警示視窗

        private void button_cancel_Click(object sender, EventArgs e)
        {
            if (currentOperation == "Add")
            {
                //取消新增:清除panel_info上已填選資料;返回Form_member介面
                DialogResult add_result = MessageBox.Show("您確定要取消新增嗎?", "取消新增", MessageBoxButtons.YesNo, MessageBoxIcon.Question);
                if (add_result == DialogResult.Yes)
                {
                    shouldPerformOperation = true;
                    Clear_panel_info();
                    Renew();
                }
                else
                {
                    shouldPerformOperation = false;

                }

            }
            else if (currentOperation == "Revise")
            {
                DialogResult add_result = MessageBox.Show("您確定要取消修改嗎?", "取消修改", MessageBoxButtons.YesNo, MessageBoxIcon.Question);
                if (add_result == DialogResult.Yes)
                {
                    shouldPerformOperation = true;
                    Clear_panel_info();
                    Renew();
                }
                else
                {
                    shouldPerformOperation = false;

                }
            }
            else if (currentOperation == "Delete")
            {
                DialogResult add_result = MessageBox.Show("不刪除嗎?", "取消刪除", MessageBoxButtons.YesNo, MessageBoxIcon.Question);
                if (add_result == DialogResult.Yes)
                {
                    shouldPerformOperation = true;
                    Clear_panel_info();
                    Renew();
                }
                else
                {
                    shouldPerformOperation = false;

                }
            }
        } //取消動作

        private void radioButton_user_CheckedChanged(object sender, EventArgs e)
        {
            if (radioButton_user.Checked)
            {
                identity = radioButton_user.Text;
            }
        } //radio的判別
        private void radioButton_manager_CheckedChanged(object sender, EventArgs e)
        {
            if (radioButton_manager.Checked)
            {
                identity = radioButton_manager.Text;
            }
        }//radio的判別

        private void button_clear_Click(object sender, EventArgs e)
        {
            textBox_numC.Text = string.Empty;
            textBox_nameC.Text = string.Empty;
            textBox_cardnumC.Text = string.Empty;
            radioButton_userC.Checked = true;
            comboBox_departC.Text = string.Empty;
            textBox_idnumC.Text = string.Empty;
            textBox_phoneC.Text = string.Empty;
        } //清除搜尋欄位已填選資料

        private void button_export_Click(object sender, EventArgs e)
        {
            try
            {
                DataTable dt = new();
                foreach (DataGridViewColumn col in dataGridView_SQL.Columns)
                {
                    dt.Columns.Add(col.HeaderText);
                }
                foreach (DataGridViewRow row in dataGridView_SQL.Rows)
                {
                    DataRow dr = dt.NewRow();
                    SQL_Conn.cn.Close();
                    for (int i = 0; i < row.Cells.Count; i++)
                    {
                        dr[i] = row.Cells[i].Value;
                    }

                    dt.Rows.Add(dr);
                }
                address_book.ExportToCsv(dt);
            }
            catch (Exception ex)
            {
                LogRecord.WriteLog(ex.Message, "form_member");
            }
            SQL_Conn.cn.Close();
        }  //導出csv

        private void Clear_panel_info()
        {   //會員資料
            textBox_num.Text = string.Empty;
            textBox_name.Text = string.Empty;
            textBox_cardnum.Text = string.Empty;
            radioButton_user.Checked = false;
            radioButton_manager.Checked = false;
            comboBox_depart.Text = "辦公室";
            comboBox_marry.Text = "單身";
            comboBox_gender.Text = "男";
            textBox_idnum.Text = string.Empty;
            textBox_postcode.Text = string.Empty;
            textBox_address.Text = string.Empty;
            textBox_phone.Text = string.Empty;
            textBox_hphone.Text = string.Empty;
            textBox_note.Text = string.Empty;
            dateTimePicker_birth.Text = default;
            dateTimePicker_entrant.Text = default;
            dateTimePicker_resign.Text = default;
            //門禁
            /*
            checkBox_door_permission.Checked = false;
            dateTimePicker_start.Value = default;
            dateTimePicker_deadline.Value = default;
            dateTimePicker_deadlineT.Value = default;
            */
        } //清除會員資料欄位

        private void Fill_panel_info()
        {


            if (dataGridView_SQL.SelectedRows.Count > 0)
            {
                // 獲取所選擇行的值
                int selectedRowIndex = dataGridView_SQL.SelectedRows[0].Index;
                int selectedID = Convert.ToInt32(dataGridView_SQL.Rows[selectedRowIndex].Cells[0].Value);

                MySqlCommand cmd = new MySqlCommand("SELECT * FROM `asc_access`.`name_list` WHERE Num = @Num", SQL_Conn.cn);
                cmd.Parameters.AddWithValue("@Num", selectedID);
                MySqlCommand cmd2 = new MySqlCommand("SELECT * FROM `asc_access`.`door_permission` WHERE CardNum = @CardNum", SQL_Conn.cn);
                cmd2.Parameters.AddWithValue("@CardNum", textBox_cardnum.Text);

                SQL_Conn.cn.Open();
                MySqlDataReader reader = cmd.ExecuteReader();
                if (reader.Read())
                {
                    textBox_num.Text = reader["Num"].ToString();
                    textBox_name.Text = reader["Name"].ToString();
                    textBox_cardnum.Text = reader["CardNum"].ToString();
                    identity = reader["Identity"].ToString();
                    dateTimePicker_birth.Text = reader["Birth"].ToString();
                    textBox_idnum.Text = reader["IDNum"].ToString();
                    textBox_postcode.Text = reader["Postcode"].ToString();
                    textBox_address.Text = reader["Address"].ToString();
                    textBox_phone.Text = reader["Phone"].ToString();
                    textBox_hphone.Text = reader["HPhone"].ToString();
                    dateTimePicker_entrant.Text = reader["Entrant"].ToString();
                    dateTimePicker_resign.Text = reader["Resign"].ToString();
                    comboBox_depart.Text = reader["Depart"].ToString();
                    comboBox_marry.Text = reader["Marry"].ToString();
                    comboBox_gender.Text = reader["Gender"].ToString();
                    textBox_note.Text = reader["Note"].ToString();

                    if (identity == "使用者")
                    {
                        radioButton_user.Checked = true;
                    }
                    else if (identity == "管理者")
                    {
                        radioButton_manager.Checked = true;
                    }
                    else if (identity == null)
                    {
                        radioButton_user.Checked = false;
                        radioButton_manager.Checked = false;
                    }

                }
                reader.Close();
                MySqlDataReader reader2 = cmd2.ExecuteReader();
                if (reader2.Read())
                {
                    dateTimePicker_start.Text = reader2["Start_Date"].ToString();
                    dateTimePicker_deadline.Text = reader2["End_Date"].ToString();
                    dateTimePicker_deadlineT.Text = reader2["End_Time"].ToString();
                    string Enable = reader2["Enable"].ToString();
                    if (Enable == "1")
                    {
                        checkBox_door_permission.Checked = true;
                    }
                    else
                    {
                        checkBox_door_permission.Checked = false;
                    }
                }
                reader2.Close();
                SQL_Conn.cn.Close();
            }

        } //將在Gridview選取行(預設只能選一行)資料帶入到panel_info的項目內

        private void button_check_Click(object sender, EventArgs e)
        {
            // 搜尋條件去頭尾空白
            string num = textBox_numC.Text.Trim();
            string name = textBox_nameC.Text.Trim();
            string cardNum = textBox_cardnumC.Text.Trim();
            string depart = comboBox_departC.Text.Trim();
            string idNum = textBox_idnumC.Text.Trim();
            string phone = textBox_phoneC.Text.Trim();

            // 編寫模糊查詢的SQL語句
            string query = "SELECT * FROM `asc_access`.`name_list` WHERE 1=1";

            if (!string.IsNullOrWhiteSpace(textBox_numC.Text))
            {
                query += $" AND Num LIKE '%{textBox_numC.Text}%'";
            }
            if (!string.IsNullOrWhiteSpace(textBox_nameC.Text))
            {
                query += $" AND Name LIKE '%{textBox_nameC.Text}%'";
            }
            if (!string.IsNullOrWhiteSpace(textBox_cardnumC.Text))
            {
                query += $" AND CardNum LIKE '%{textBox_cardnumC.Text}%'";
            }
            if (!string.IsNullOrWhiteSpace(comboBox_departC.Text))
            {
                query += $" AND Depart LIKE '%{comboBox_departC.Text}%'";
            }
            if (!string.IsNullOrWhiteSpace(textBox_idnumC.Text))
            {
                query += $" AND IDNum LIKE '%{textBox_idnumC.Text}%'";
            }
            if (!string.IsNullOrWhiteSpace(textBox_phoneC.Text))
            {
                query += $" AND Phone LIKE '%{textBox_phoneC.Text}%'";
            }

            //如果欄位不是空值就把輸入值加到command裡
            {
                MySqlCommand cmd = new MySqlCommand(query, SQL_Conn.cn);
                SQL_Conn.cn.Open();
                if (!string.IsNullOrEmpty(num)) { cmd.Parameters.AddWithValue("@Num", num); }
                if (!string.IsNullOrEmpty(name)) { cmd.Parameters.AddWithValue("@Name", name); }
                if (!string.IsNullOrEmpty(cardNum)) { cmd.Parameters.AddWithValue("@CardNum", cardNum); }
                if (!string.IsNullOrEmpty(depart)) { cmd.Parameters.AddWithValue("@Depart", depart); }
                if (!string.IsNullOrEmpty(idNum)) { cmd.Parameters.AddWithValue("@IDNum", idNum); }
                if (!string.IsNullOrEmpty(phone)) { cmd.Parameters.AddWithValue("@Phone", phone); }

                MySqlDataReader reader = cmd.ExecuteReader();
                dataGridView_SQL.Rows.Clear(); //清掉原本的顯示資料
                while (reader.Read())
                {
                    int index = this.dataGridView_SQL.Rows.Add();

                    this.dataGridView_SQL.Rows[index].Cells[0].Value = reader.GetString("Num");
                    this.dataGridView_SQL.Rows[index].Cells[1].Value = reader.GetString("Name");
                    this.dataGridView_SQL.Rows[index].Cells[2].Value = reader.GetString("CardNum");
                    this.dataGridView_SQL.Rows[index].Cells[3].Value = reader.GetString("Identity");
                    this.dataGridView_SQL.Rows[index].Cells[4].Value = reader.GetDateTime("Birth");
                    this.dataGridView_SQL.Rows[index].Cells[5].Value = reader.GetString("IDNum");
                    this.dataGridView_SQL.Rows[index].Cells[6].Value = reader.GetString("Postcode");
                    this.dataGridView_SQL.Rows[index].Cells[7].Value = reader.GetString("Address");
                    this.dataGridView_SQL.Rows[index].Cells[8].Value = reader.GetString("Phone");
                    this.dataGridView_SQL.Rows[index].Cells[9].Value = reader.GetString("HPhone");
                    this.dataGridView_SQL.Rows[index].Cells[10].Value = reader.GetDateTime("Entrant");
                    this.dataGridView_SQL.Rows[index].Cells[11].Value = reader.GetDateTime("Resign");
                    this.dataGridView_SQL.Rows[index].Cells[12].Value = reader.GetString("Depart");
                    this.dataGridView_SQL.Rows[index].Cells[13].Value = reader.GetString("Marry");
                    this.dataGridView_SQL.Rows[index].Cells[14].Value = reader.GetString("Gender");
                    this.dataGridView_SQL.Rows[index].Cells[15].Value = reader.GetString("Note");
                }
                reader.Close();
                cmd.ExecuteNonQuery();
                SQL_Conn.cn.Close();
            }
        } //點擊查詢按鈕事件

        private void button_photo_Click(object sender, EventArgs e)
        {
            PhotoId = this.textBox_num.Text; //綁定工號為照片ID
            if (!string.IsNullOrEmpty(textBox_num.Text))
            {
                if (pictureBox_photo.Image == null)
                {
                    OpenFileDialog openFileDialog = new OpenFileDialog();
                    openFileDialog.Filter = "Image Files (*.bmp;*.jpg;*.jpeg,*.png)|*.BMP;*.JPG;*.JPEG;*.PNG";
                    if (openFileDialog.ShowDialog() == DialogResult.OK)
                    {
                        // 讀取選擇的圖片並轉換成二進制數據
                        byte[] imageData;
                        using (MemoryStream ms = new MemoryStream())
                        {
                            using (Image image = Image.FromFile(openFileDialog.FileName))
                            {
                                // 將圖片壓縮成JPEG格式
                                ImageCodecInfo jpgEncoder = GetEncoder(ImageFormat.Jpeg);
                                EncoderParameters encoderParams = new EncoderParameters(1);
                                encoderParams.Param[0] = new EncoderParameter(System.Drawing.Imaging.Encoder.Quality, 80L);
                                image.Save(ms, jpgEncoder, encoderParams);
                            }
                            imageData = ms.ToArray();
                        }


                        // 將圖片數據上傳到資料庫
                        MySqlCommand cmd = new MySqlCommand("INSERT INTO `asc_access`.`photos` (Photo, PhotoId) VALUES (@image_data, @photoid)", SQL_Conn.cn);
                        SQL_Conn.cn.Open();
                        cmd.Parameters.AddWithValue("@image_data", imageData);
                        cmd.Parameters.AddWithValue("@photoid", PhotoId);
                        cmd.ExecuteNonQuery();

                        // 顯示選擇的圖片
                        pictureBox_photo.Image = Image.FromFile(openFileDialog.FileName);
                    }
                }
                else
                {
                    OpenFileDialog openFileDialog = new OpenFileDialog();
                    openFileDialog.Filter = "Image Files (*.bmp;*.jpg;*.jpeg,*.png)|*.BMP;*.JPG;*.JPEG;*.PNG";
                    if (openFileDialog.ShowDialog() == DialogResult.OK)
                    {
                        // 讀取選擇的圖片並轉換成二進制數據
                        byte[] imageData;
                        using (MemoryStream ms = new MemoryStream())
                        {
                            using (Image image = Image.FromFile(openFileDialog.FileName))
                            {
                                // 將圖片壓縮成JPEG格式
                                ImageCodecInfo jpgEncoder = GetEncoder(ImageFormat.Jpeg);
                                EncoderParameters encoderParams = new EncoderParameters(1);
                                encoderParams.Param[0] = new EncoderParameter(System.Drawing.Imaging.Encoder.Quality, 80L);
                                image.Save(ms, jpgEncoder, encoderParams);
                            }
                            imageData = ms.ToArray();
                        }
                        // 將圖片數據更新到資料庫
                        MySqlCommand updatePhotoCommand = new("UPDATE `asc_access`.`photos` SET Photo = @image_data WHERE PhotoId = @photoid", SQL_Conn.cn);
                        SQL_Conn.cn.Open();
                        updatePhotoCommand.Parameters.AddWithValue("@image_data", imageData);
                        updatePhotoCommand.Parameters.AddWithValue("@photoid", PhotoId);
                        updatePhotoCommand.ExecuteNonQuery();

                        pictureBox_photo.Image = Image.FromFile(openFileDialog.FileName);
                    }
                }
            }
            else
            {
                MessageBox.Show("請先輸入工號");
                return;
            }
            SQL_Conn.cn.Close();

        } //上傳並顯示上傳的照片(原本有就更新)(只存一張)

        private void button_showPhoto_Click(object sender, EventArgs e)
        {
            if (!string.IsNullOrEmpty(textBox_num.Text))
            {
                if (pictureBox_photo.Image == null)
                {
                    MySqlCommand cmd = new("SELECT `Photo` FROM `asc_access`.`photos` WHERE PhotoId = @photoid", SQL_Conn.cn);
                    SQL_Conn.cn.Open();
                    PhotoId = this.textBox_num.Text;
                    cmd.Parameters.AddWithValue("@photoid", PhotoId);
                    byte[]? imageData = cmd.ExecuteScalar() as byte[];
                    if (imageData != null && imageData.Length > 0)
                    {
                        using (MemoryStream stream = new MemoryStream(imageData))
                        {
                            pictureBox_photo.Image = Image.FromStream(stream);
                        }
                    }
                    else
                    {
                        MessageBox.Show("找不到對應的照片。");
                    }
                }
                else
                {
                    MessageBox.Show("照片已顯示");
                    return;
                }
            }
            else
            {
                MessageBox.Show("請先輸入工號");
                return;
            }
            SQL_Conn.cn.Close();
        } //依照工號顯示對應照片

        private ImageCodecInfo? GetEncoder(ImageFormat format)
        {
            ImageCodecInfo[] codecs = ImageCodecInfo.GetImageDecoders();
            foreach (ImageCodecInfo codec in codecs)
            {
                if (codec.FormatID == format.Guid)
                {
                    return codec;
                }
            }
            return null;
        }//獲取JPEG編碼器

        private void textBox_pwd_TextChanged(object sender, EventArgs e)
        {
            textBox_pwd.KeyDown -= panel_info_KeyDown;
            textBox_pwd.KeyDown += panel_info_KeyDown;
            textBox_pwd.UseSystemPasswordChar = true;
            textBox_pwd.PasswordChar = '●'; // 密碼顯示為 '●'
        }


        private void button_pwd_check_Click(object sender, EventArgs e)
        {
            AccountValidator validator = new();
            string account = Form_Login.LoggedInAccount;
            Debug.WriteLine("account : " + account);
            string password = textBox_pwd.Text.Trim();
            Debug.WriteLine("password : " + password);
            SQL_Conn.cn.Open();
            if (validator.Validate(account, password))
            {
                panel5.Enabled = true;
                textBox_pwd.Text = string.Empty;
            }
            else
            {
                LogRecord.WriteLog(textBox_pwd.Text, "form_member_panel_info");
                MessageBox.Show("請確認密碼", "錯誤", MessageBoxButtons.OK, MessageBoxIcon.Error);
                Debug.WriteLine(textBox_pwd.Text);
                textBox_pwd.Clear();
            }
            SQL_Conn.cn.Close();
        }
        private void panel_info_KeyDown(object sender, KeyEventArgs e)
        {
            if (e.KeyCode == Keys.Enter)
            {
                if (!string.IsNullOrEmpty(textBox_pwd.Text))
                {
                    button_pwd_check.PerformClick();
                }
            }
        }
    }
}
