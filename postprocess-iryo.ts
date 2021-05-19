import { xlsx, readXLSX, writeCSV } from "https://deno.land/x/flat@0.0.10/mod.ts";

const inputFilename = Deno.args[0];
const outputFilename = inputFilename.replace(".xlsx", ".csv");

// read about what the xlsx library can do here: https://github.com/SheetJS/sheetjs

const workbook = await readXLSX(inputFilename);
const sheetData = workbook.Sheets[workbook.SheetNames[0]];
const csvString = await xlsx.utils.sheet_to_csv(sheetData); // can use to_json, to_txt, to_html, to_formulae

// write to csv
await writeCSV(outputFilename, csvString);