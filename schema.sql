drop table if exists legend;
	create table legend (
	var_name string primary key,
	var_desc string
);

drop table if exists penn;
	create table penn (
	country text primary key,
	year integer not null,
	rgdpna Decimal, -- Real GDP PPP 2005 $$ 
	pop integer, -- population
	ck Decimal, -- capital stock 
	hc Decimal, -- educational attainment
	csh_x Decimal, -- exports
	csh_m Decimal -- imports
);

drop table if exists penn_complete;
	create table penn_complete (
	country text primary key
);