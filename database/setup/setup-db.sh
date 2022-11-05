for i in {1..50};
do
    if [ ! -f 0_main.sql ]; then
        echo "setup completed"
        break
    fi

    /opt/mssql-tools/bin/sqlcmd -S localhost -U sa -P $SA_PASSWORD -d master -i 0_main.sql

    if [ $? -eq 0 ]
    then
        rm 0_main.sql
    else
        echo "not ready yet..."
        sleep 1
    fi
done