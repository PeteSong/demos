import com.github.spotbugs.snom.Confidence
import com.github.spotbugs.snom.Effort
import com.github.spotbugs.snom.SpotBugsTask

plugins {
    id("java")

    id("application")
    id("jacoco")
    id("checkstyle")
    id("com.github.spotbugs") version "6.0.26"
    id("pmd")
}

group = "io.petesong"
version = "1.0-SNAPSHOT"

repositories {
    mavenCentral()
}

java {
    toolchain {
        languageVersion = JavaLanguageVersion.of(21)
    }
}

tasks.withType<JavaCompile> {
    sourceCompatibility = "21"
    targetCompatibility = "21"
}

dependencies {
    testImplementation(platform("org.junit:junit-bom:5.11.3"))
    testImplementation("org.junit.jupiter:junit-jupiter")
    testRuntimeOnly("org.junit.platform:junit-platform-launcher")

    compileOnly("org.projectlombok:lombok:1.18.36")
    annotationProcessor("org.projectlombok:lombok:1.18.36")

    testCompileOnly("org.projectlombok:lombok:1.18.36")
    testAnnotationProcessor("org.projectlombok:lombok:1.18.36")
}

jacoco {
    toolVersion = "0.8.12"
}

checkstyle {
    toolVersion = "10.20.2"
    configFile = file("config/checkstyle/google_checks.xml")
    isIgnoreFailures = false
}

spotbugs {
    toolVersion = "4.8.6"
    effort = Effort.DEFAULT
    reportLevel = Confidence.DEFAULT
    ignoreFailures = false
}

pmd {
    toolVersion = "7.8.0"
}

tasks.test {
    useJUnitPlatform()
    finalizedBy("jacocoTestReport")
    testLogging {
        events("passed", "skipped", "failed")
        showStandardStreams = true
    }
}

tasks.jacocoTestReport {
    dependsOn(tasks.test)
    reports {
        html.required.set(true)
    }
}

tasks.jacocoTestCoverageVerification {
    violationRules {
        rule {
            limit {
                counter = "LINE"
                value = "COVEREDRATIO"
                minimum = 0.90.toBigDecimal()
            }
            limit {
                counter = "BRANCH"
                value = "COVEREDRATIO"
                minimum = 0.90.toBigDecimal()
            }
        }
    }
}

tasks.withType<Checkstyle> {
    reports {
        html.required.set(true)
    }
}

tasks.withType<SpotBugsTask> {
    reports.create("html") {
        required = true
        outputLocation = file(layout.buildDirectory.dir("reports/spotbugs.html"))
        setStylesheet("fancy-hist.xsl")
    }
}

tasks.check {
    dependsOn(tasks.jacocoTestCoverageVerification)
}

application {
    mainClass = "io.petesong.Main"
}

tasks.register<JavaExec>("runClass") {
    val className = project.findProperty("className")?.toString() ?: "io.petesong.Main"
    mainClass.set(className)
    classpath = sourceSets["main"].runtimeClasspath
}
