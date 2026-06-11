mkdir -p "$(pwd)/data"
mkdir -p "$(pwd)/local_data"
build_generator() {
    docker build -t datagen ./generator
}
run_generator() {
    docker run -v "$(pwd)/data":/data datagen
}
create_local_data() {
    python3 generator/generate.py "$(pwd)/local_data"
}
build_reporter() {
    docker build -t datarep ./reporter
}
run_reporter() {
    docker run -v "$(pwd)/data":/data datarep
}
"$@"