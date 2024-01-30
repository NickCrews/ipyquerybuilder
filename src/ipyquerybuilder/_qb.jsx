import { QueryBuilder } from 'react-querybuilder';
// import MuiQueryBuilder from "mui-querybuilder";
import { createTheme, ThemeProvider } from '@mui/material/styles';
import { QueryBuilderMaterial } from '@react-querybuilder/material';
import React from 'react';



const muiTheme = createTheme();

export default function ({ _fields, set__fields, _query, set__query, show_not_toggle, set_show_not_toggle, debug }) {
    return <ThemeProvider theme={muiTheme}>
        <QueryBuilderMaterial>
            <QueryBuilder
                fields={_fields}
                query={_query}
                onQueryChange={q => set__query(q)}
                showNotToggle={show_not_toggle}
            />
        </QueryBuilderMaterial>
    </ThemeProvider>
};