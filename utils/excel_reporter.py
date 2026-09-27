from pathlib import Path
from openpyxl import load_workbook
from openpyxl.styles import Font, PatternFill, Alignment


# ============================================================
# FILE LOCATIONS
# ============================================================

PROJECT_ROOT = Path(__file__).resolve().parent.parent

MASTER_FILE = (
    PROJECT_ROOT
    / "test_data"
    / "saucedemo_complete_test_case_master.xlsx"
)

REPORT_DIR = PROJECT_ROOT / "reports"
REPORT_FILE = REPORT_DIR / "test_results.xlsx"


# ============================================================
# TEST NAME → TEST CASE ID MAPPING
# ============================================================

TEST_CASE_MAP = {

    # ---------------- LOGIN ----------------
    "test_valid_login": "TC_LOGIN_001",

    "test_invalid_login[chromium-wrong_user-secret_sauce]":
        "TC_LOGIN_002",

    "test_invalid_login[chromium-standard_user-wrong_password]":
        "TC_LOGIN_003",

    "test_invalid_login[chromium-wrong_user-wrong_password]":
        "TC_LOGIN_004",

    # ---------------- INVENTORY ----------------
    "test_product_can_be_added_to_cart[Sauce Labs Backpack]":
        "TC_INV_002",

    "test_product_can_be_added_to_cart[Sauce Labs Bike Light]":
        "TC_INV_003",

    "test_product_can_be_added_to_cart[Sauce Labs Bolt T-Shirt]":
        "TC_INV_007",

    "test_product_can_be_added_to_cart[Sauce Labs Fleece Jacket]":
        "TC_INV_007",

    "test_product_can_be_added_to_cart[Sauce Labs Onesie]":
        "TC_INV_007",

    "test_product_can_be_added_to_cart[Test.allTheThings() T-Shirt (Red)]":
        "TC_INV_007",

    "test_sort_products_high_to_low":
        "TC_INV_005",

    # ---------------- CART ----------------
    "test_cart_contains_selected_product":
        "TC_CART_001",

    "test_cart_contains_multiple_products":
        "TC_CART_003",

    "test_cart_product_names":
        "TC_CART_001",

    "test_cart_product_quantity":
        "TC_CART_004",

    # ---------------- CHECKOUT ----------------
    "test_checkout_required_fields[chromium--Mateti-12345-Error: First Name is required]":
        "TC_CHK_002",

    "test_checkout_required_fields[chromium-Anusha--12345-Error: Last Name is required]":
        "TC_CHK_003",

    "test_checkout_required_fields[chromium-Anusha-Mateti--Error: Postal Code is required]":
        "TC_CHK_004",

    # ---------------- E2E ----------------
    "test_user_can_add_product_to_cart[chromium]":
        "TC_E2E_001",

    "test_sort_products_high_to_low":
        "TC_INV_005",
}


# ============================================================
# LOAD MASTER TEST CASES
# ============================================================

def load_master_test_cases():

    if not MASTER_FILE.exists():

        raise FileNotFoundError(
            f"\nMaster test case file not found:\n"
            f"{MASTER_FILE}\n\n"
            f"Please place "
            f"'saucedemo_complete_test_case_master.xlsx' "
            f"inside the test_data folder."
        )

    workbook = load_workbook(
        MASTER_FILE,
        data_only=True
    )

    worksheet = workbook["All Test Cases"]

    test_cases = {}

    headers = [
        cell.value
        for cell in worksheet[1]
    ]

    for row in worksheet.iter_rows(
        min_row=2,
        values_only=True
    ):

        if not row[0]:
            continue

        test_case = dict(
            zip(headers, row)
        )

        test_cases[
            test_case["Test Case ID"]
        ] = test_case

    workbook.close()

    return test_cases


# ============================================================
# FIND TEST CASE ID
# ============================================================

def get_test_case_id(nodeid):

    # Remove tests/ path
    test_name = nodeid.split("::")[-1]

    # Exact mapping
    if test_name in TEST_CASE_MAP:

        return TEST_CASE_MAP[test_name]

    # Handle parameterized tests more flexibly

    if "test_invalid_login" in test_name:

        if "wrong_user-secret_sauce" in test_name:
            return "TC_LOGIN_002"

        if "standard_user-wrong_password" in test_name:
            return "TC_LOGIN_003"

        if "wrong_user-wrong_password" in test_name:
            return "TC_LOGIN_004"

    if "test_checkout_required_fields" in test_name:

        if "--Mateti-12345" in test_name:
            return "TC_CHK_002"

        if "Anusha--12345" in test_name:
            return "TC_CHK_003"

        if "Anusha-Mateti--" in test_name:
            return "TC_CHK_004"

    if "test_product_can_be_added_to_cart" in test_name:

        return "TC_INV_007"

    if "test_user_can_add_product_to_cart" in test_name:

        return "TC_E2E_001"

    if "test_sort_products_high_to_low" in test_name:

        return "TC_INV_005"

    return None


# ============================================================
# CREATE EXECUTION REPORT
# ============================================================

def create_excel_report(results):

    REPORT_DIR.mkdir(
        parents=True,
        exist_ok=True
    )

    master_cases = load_master_test_cases()

    workbook = load_workbook(
        MASTER_FILE
    )

    # ========================================================
    # REMOVE OLD EXECUTION SHEETS
    # ========================================================

    if "Execution Results" in workbook.sheetnames:

        del workbook["Execution Results"]

    if "Execution Summary" in workbook.sheetnames:

        del workbook["Execution Summary"]

    # ========================================================
    # EXECUTION RESULTS
    # ========================================================

    ws = workbook.create_sheet(
        "Execution Results"
    )

    headers = [
        "Test Case ID",
        "Module",
        "Test Scenario",
        "Automation Status",
        "Execution Status",
        "Test Name",
        "Duration (sec)",
        "Error",
    ]

    ws.append(headers)

    # ========================================================
    # INITIALIZE ALL MASTER TEST CASES
    # ========================================================

    execution_data = {}

    for test_case_id, test_case in master_cases.items():

        execution_data[test_case_id] = {
            "module": test_case["Module"],
            "scenario": test_case["Test Scenario"],
            "automation_status": test_case["Automation Status"],
            "status": "NOT EXECUTED",
            "test_name": "",
            "duration": "",
            "error": "",
        }

    # ========================================================
    # UPDATE WITH PYTEST RESULTS
    # ========================================================

    for result in results:

        test_case_id = get_test_case_id(
            result["test_name"]
        )

        if not test_case_id:
            continue

        if test_case_id not in execution_data:
            continue

        current = execution_data[test_case_id]

        # If same test case has multiple parameterized tests,
        # keep the most serious result.
        status = result["status"]

        priority = {
            "FAIL": 4,
            "ERROR": 3,
            "PASS": 2,
            "SKIP": 1,
            "NOT EXECUTED": 0,
        }

        if priority.get(status, 0) >= priority.get(
            current["status"],
            0
        ):

            current["status"] = status

        current["test_name"] = result["test_name"]
        current["duration"] = result["duration"]
        current["error"] = result["error"]

    # ========================================================
    # WRITE ALL MASTER TEST CASES
    # ========================================================

    for test_case_id, data in execution_data.items():

        ws.append([
            test_case_id,
            data["module"],
            data["scenario"],
            data["automation_status"],
            data["status"],
            data["test_name"],
            data["duration"],
            data["error"],
        ])

    # ========================================================
    # EXECUTION SUMMARY
    # ========================================================

    summary = workbook.create_sheet(
        "Execution Summary"
    )

    total = len(execution_data)

    passed = sum(
        1
        for data in execution_data.values()
        if data["status"] == "PASS"
    )

    failed = sum(
        1
        for data in execution_data.values()
        if data["status"] == "FAIL"
    )

    errors = sum(
        1
        for data in execution_data.values()
        if data["status"] == "ERROR"
    )

    skipped = sum(
        1
        for data in execution_data.values()
        if data["status"] == "SKIP"
    )

    not_executed = sum(
        1
        for data in execution_data.values()
        if data["status"] == "NOT EXECUTED"
    )

    executed = (
        passed
        + failed
        + errors
        + skipped
    )

    pass_rate = (
        passed / executed * 100
        if executed
        else 0
    )

    summary.append([
        "Metric",
        "Value"
    ])

    summary.append([
        "Total Test Cases",
        total
    ])

    summary.append([
        "Executed",
        executed
    ])

    summary.append([
        "Passed",
        passed
    ])

    summary.append([
        "Failed",
        failed
    ])

    summary.append([
        "Errors",
        errors
    ])

    summary.append([
        "Skipped",
        skipped
    ])

    summary.append([
        "Not Executed",
        not_executed
    ])

    summary.append([
        "Pass Rate",
        f"{pass_rate:.2f}%"
    ])

    # ========================================================
    # MODULE SUMMARY
    # ========================================================

    module_summary = workbook.create_sheet(
        "Module Summary"
    )

    module_summary.append([
        "Module",
        "Total",
        "Executed",
        "Passed",
        "Failed",
        "Errors",
        "Skipped",
        "Not Executed",
        "Pass Rate",
    ])

    modules = sorted(
        set(
            data["module"]
            for data in execution_data.values()
        )
    )

    for module in modules:

        module_cases = [
            data
            for data in execution_data.values()
            if data["module"] == module
        ]

        module_total = len(module_cases)

        module_passed = sum(
            1
            for data in module_cases
            if data["status"] == "PASS"
        )

        module_failed = sum(
            1
            for data in module_cases
            if data["status"] == "FAIL"
        )

        module_errors = sum(
            1
            for data in module_cases
            if data["status"] == "ERROR"
        )

        module_skipped = sum(
            1
            for data in module_cases
            if data["status"] == "SKIP"
        )

        module_not_executed = sum(
            1
            for data in module_cases
            if data["status"] == "NOT EXECUTED"
        )

        module_executed = (
            module_passed
            + module_failed
            + module_errors
            + module_skipped
        )

        module_pass_rate = (
            module_passed / module_executed * 100
            if module_executed
            else 0
        )

        module_summary.append([
            module,
            module_total,
            module_executed,
            module_passed,
            module_failed,
            module_errors,
            module_skipped,
            module_not_executed,
            f"{module_pass_rate:.2f}%"
        ])

    # ========================================================
    # FORMATTING
    # ========================================================

    for sheet in [
        ws,
        summary,
        module_summary
    ]:

        for cell in sheet[1]:

            cell.font = Font(
                bold=True
            )

            cell.fill = PatternFill(
                fill_type="solid",
                fgColor="D9EAF7"
            )

            cell.alignment = Alignment(
                horizontal="center",
                vertical="center"
            )

        sheet.freeze_panes = "A2"

        for row in sheet.iter_rows():

            for cell in row:

                cell.alignment = Alignment(
                    vertical="top",
                    wrap_text=True
                )

    # ========================================================
    # STATUS COLORS
    # ========================================================

    status_colors = {
        "PASS": "C6EFCE",
        "FAIL": "FFC7CE",
        "ERROR": "FFC7CE",
        "SKIP": "FFEB9C",
        "NOT EXECUTED": "D9E1F2",
    }

    for row in ws.iter_rows(
        min_row=2
    ):

        status_cell = row[4]

        color = status_colors.get(
            status_cell.value
        )

        if color:

            status_cell.fill = PatternFill(
                fill_type="solid",
                fgColor=color
            )

    # ========================================================
    # COLUMN WIDTHS
    # ========================================================

    widths = {
        "A": 18,
        "B": 18,
        "C": 40,
        "D": 20,
        "E": 18,
        "F": 70,
        "G": 18,
        "H": 80,
    }

    for column, width in widths.items():

        ws.column_dimensions[column].width = width

    summary.column_dimensions["A"].width = 25
    summary.column_dimensions["B"].width = 20

    for column in "ABCDEFGHI":

        module_summary.column_dimensions[
            column
        ].width = 18

    # ========================================================
    # SAVE
    # ========================================================

    workbook.save(
        REPORT_FILE
    )

    print(
        f"\nExcel execution report created:"
        f"\n{REPORT_FILE}"
    )

    return REPORT_FILE