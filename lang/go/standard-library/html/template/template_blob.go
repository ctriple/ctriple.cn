package main

import (
	"html/template"
	"log"
	"os"
	"strings"
)

func main() {
	const (
		master  = `Name:{{block "list" .}}{{"\n"}}{{range .}}{{println "-" .}}{{end}}{{end}}`
		overlay = `{{define "list"}} {{join . ", "}}{{end}}`
	)
	var (
		funcs     = template.FuncMap{"join": strings.Join}
		guardians = []string{"Gamora", "Groot", "Nebula", "Rocket", "Star-Loard"}
	)
	masterTmpl, err := template.New("master").Funcs(funcs).Parse(master)
	if err != nil {
		log.Fatal(err)
	}
	overlayTmpl, err := template.Must(masterTmpl.Clone()).Parse(overlay)
	if err != nil {
		log.Fatal(err)
	}
	if err := masterTmpl.Execute(os.Stdout, guardians); err != nil {
		log.Fatal(err)
	}
	if err := overlayTmpl.Execute(os.Stdout, guardians); err != nil {
		log.Fatal(err)
	}
}
