drop table if exists legend;
	create table legend (
	var_name string primary key,
	var_desc string
);

drop table if exists penn;
	create table penn (
	country text primary key,
	year integer not null,
	gdp Decimal, -- Real GDP PPP 2005 $$, rgdpna
	pop integer, -- population, pop
	capital Decimal, -- capital stock, ck
	school Decimal, -- educational attainment, hc
	trade Decimal  -- csh_h + csh+r
);